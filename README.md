# Cityscape CycleGAN: Day & Night Translation 

> University assignment implementing CycleGAN for unpaired day-to-night and night-to-day image translation. These Jupyter notebooks are tuned for high-resolution, highly detailed cityscape photography, focusing on preserving complex lighting and architectural structures.

---


##  Key Features

* **High-Resolution Processing:** Optimized to handle detailed urban textures and complex geometries without severe artifacting.
* **Unpaired Translation:** Utilizes Cycle-Consistency loss to train on unpaired daylight and nighttime datasets.
* **Interactive Notebooks:** Step-by-step Jupyter Notebooks documenting dataset building, training loops, and inference.

---

##  Repository Structure

* `01_build_dataset.ipynb`: Notebook for preparing, formatting, and structuring the high-resolution cityscape datasets.
* `02_train_cyclegan.ipynb`: Contains the CycleGAN architecture definitions, loss tracking, and the main training loop.
* `03_inference_results.ipynb`: Notebook for running the trained model on test data and visualizing the day-to-night and night-to-day conversions.
* `/scripts/`: Directory for auxiliary Python scripts and helper functions.
* `/results/`: Directory for storing the generated output images and translation results.
* `/data/`: Directory where the training and testing images are located. Data is available under following link: [DATA](https://drive.google.com/drive/folders/1Pqu6_HBOFDfSVwzidlauE4zCyt1rAXBU?usp=sharing)
* `/checkpoints/`: Directory for saving and loading model weights during the training process. Checkpoints are available under following link: [CHECKPOINTS](https://drive.google.com/drive/folders/1YLYC889vXjaXbpsDd6Xn65dXpsALBOE9?usp=sharing)

---
