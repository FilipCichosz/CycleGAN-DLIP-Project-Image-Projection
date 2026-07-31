import argparse
import os
import random

from PIL import Image, ImageDraw, ImageFilter


def make_street(size, rnd):
    base = rnd.randint(90, 130)
    img = Image.new("RGB", (size, size), (base, base, base + 5))
    px = img.load()
    for _ in range(size * size // 3):
        x, y = rnd.randint(0, size - 1), rnd.randint(0, size - 1)
        d = rnd.randint(-35, 35)
        r, g, b = px[x, y]
        px[x, y] = (max(0, min(255, r + d)),
                    max(0, min(255, g + d)),
                    max(0, min(255, b + d)))
    draw = ImageDraw.Draw(img)
    for x in range(0, size, 18):
        draw.line([(x, 0), (x, size)], fill=(70, 70, 70), width=1)
    cx, cy = rnd.randint(size // 3, 2 * size // 3), rnd.randint(size // 5, size // 2)
    draw.rectangle([cx - 30, cy - 22, cx + 30, cy + 4], outline=(200, 200, 200), width=3)
    draw.ellipse([cx - 16, cy + 4, cx + 16, cy + 20], outline=(230, 120, 40), width=4)
    return img.filter(ImageFilter.GaussianBlur(0.4))


def make_pro(size, rnd):
    base_r = rnd.randint(190, 220)
    img = Image.new("RGB", (size, size), (base_r, base_r - 40, base_r - 110))
    draw = ImageDraw.Draw(img)
    for y in range(0, size, 8):
        shade = rnd.randint(-12, 12)
        draw.line([(0, y), (size, y)],
                  fill=(base_r + shade, base_r - 40 + shade, base_r - 110 + shade),
                  width=3)
    m = rnd.randint(20, 40)
    draw.rectangle([m, m, size - m, size - m], outline=(245, 245, 245), width=4)
    cx, cy = size // 2, size // 2
    rad = rnd.randint(size // 8, size // 5)
    draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad],
                 outline=(245, 245, 245), width=4)
    draw.line([(cx, m), (cx, size - m)], fill=(245, 245, 245), width=4)
    return img.filter(ImageFilter.GaussianBlur(0.3))


def main():
    parser = argparse.ArgumentParser(description="Generator obrazow demo CycleGAN")
    parser.add_argument("--n", type=int, default=120, help="liczba obrazow na domene")
    parser.add_argument("--size", type=int, default=256)
    parser.add_argument("--root", default="data")
    args = parser.parse_args()

    rnd = random.Random(123)
    dir_a = os.path.join(args.root, "raw_street")
    dir_b = os.path.join(args.root, "raw_pro")
    os.makedirs(dir_a, exist_ok=True)
    os.makedirs(dir_b, exist_ok=True)

    for i in range(args.n):
        make_street(args.size, rnd).save(os.path.join(dir_a, f"street_{i:04d}.jpg"), quality=92)
        make_pro(args.size, rnd).save(os.path.join(dir_b, f"pro_{i:04d}.jpg"), quality=92)

    print(f"Wygenerowano {args.n} obrazow demo w kazdej domenie:")
    print(f"  {dir_a}")
    print(f"  {dir_b}")
    print("To dane SYNTETYCZNE - do oddania zadania uzyj prawdziwych zdjec.")


if __name__ == "__main__":
    main()
