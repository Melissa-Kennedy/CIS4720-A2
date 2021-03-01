# CIS4720-A2

## Function explanations

### AHE

### CLAHE

### MinMax / Global Histogram Stretching

### Local Histogram Stretching

## Checking Quality of Improved Images

### Wang's Universal Image Quality Index

`quality.py` implements Zhou Wang's Universal Image Quality Index

> [Zhou Wang and A. C. Bovik, "A universal image quality index," in IEEE Signal Processing Letters, vol. 9, no. 3, pp. 81-84, March 2002, doi: 10.1109/97.995823.](https://ieeexplore.ieee.org/abstract/document/995823)

## To run

Be in a virtual environment
```
pip install -r requirements.txt
python run.py
```

Follow prompts:

1. Prefix: Either `eg1` or `eg2`, depending on which test image you want to use.
2. Number: Some test images have a number at the end. Ex. `eg2_lowcntrst2.jpg`. In this case, 2 is the number.
3. Algorithm name: Which algoritm will be applied to the image
    - CLAHE: Contrast Limited Adaptive Histogram Equalization
    - AHE: Adaptive Histogram Equalization
    - minmax: Global Contrast Stretching
    - local: Local contrast stretching
    - all: Applies all of the above (takes a while)

After running, the edited images will be saved in the `editedImages` directory, and the image quality numbers will be printed to the console.