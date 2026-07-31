import argparse
import os
import random

from PIL import Image, ImageOps


def center_square(img):
    w, h = img.size
    s = min(w, h)
    left = (w - s) // 2
    top = (h - s) // 2
    return img.crop((left, top, left + s, top + s))


def process_domain(raw_dir, train_dir, test_dir, size, test_ratio, seed):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    files = sorted(f for f in os.listdir(raw_dir)
                   if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")))
    if not files:
        print(f"  UWAGA: brak zdjec w {raw_dir}")
        return 0, 0

    random.Random(seed).shuffle(files)
    n_test = max(1, int(len(files) * test_ratio))
    test_set = set(files[:n_test])

    n_train, n_test_done = 0, 0
    for i, fname in enumerate(files):
        src = os.path.join(raw_dir, fname)
        try:
            img = Image.open(src)
            img = ImageOps.exif_transpose(img).convert("RGB")
        except Exception as e:
            print(f"  pomijam {fname}: {e}")
            continue

        img = center_square(img).resize((size, size), Image.LANCZOS)
        dst_dir = test_dir if fname in test_set else train_dir
        img.save(os.path.join(dst_dir, f"{i:05d}.jpg"), quality=95)

        if fname in test_set:
            n_test_done += 1
        else:
            n_train += 1

    return n_train, n_test_done


def main():
    parser = argparse.ArgumentParser(description="Budowa zbioru CycleGAN")
    parser.add_argument("--root", default="data", help="katalog glowny danych")
    parser.add_argument("--size", type=int, default=256, help="docelowy rozmiar obrazu")
    parser.add_argument("--test", type=float, default=0.1, help="udzial zbioru testowego")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    root = args.root
    print("Domena A (uliczna):")
    a_tr, a_te = process_domain(
        os.path.join(root, "raw_street"),
        os.path.join(root, "trainA"),
        os.path.join(root, "testA"),
        args.size, args.test, args.seed)
    print(f"  trainA={a_tr}  testA={a_te}")

    print("Domena B (profesjonalna):")
    b_tr, b_te = process_domain(
        os.path.join(root, "raw_pro"),
        os.path.join(root, "trainB"),
        os.path.join(root, "testB"),
        args.size, args.test, args.seed)
    print(f"  trainB={b_tr}  testB={b_te}")

    print("-" * 50)
    print(f"Razem: A={a_tr + a_te}  B={b_tr + b_te}")
    print(f"Rozmiar obrazow: {args.size}x{args.size}")
    if min(a_tr, b_tr) < 100:
        print("UWAGA: malo danych (<100 na domene). Dodaj wiecej zdjec dla lepszych wynikow.")


if __name__ == "__main__":
    main()
