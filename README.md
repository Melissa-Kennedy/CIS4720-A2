# CIS4720-A2

## Function explanations

### AHE
`ahe.py` uses OpenCV's implementation of Contrast Limited Adaptive Histogram Equalization, but with a `clipLimit` of 0. In other words, it implements Adaptive Histogram Equalization. By default, it has a block size of 9x9.

### CLAHE
`clahe.py` uses OpenCV's implementation of Contrast Limited Adaptive Histogram Equalization. By default, it has a max slope of 2, and a block size of 9x9.

### MinMax / Global Histogram Stretching
the `minmax` function of `minmax.py` implements global contrast stretching.

### Local Histogram Stretching
The `local_minmax` function in `minmax.py` implements local contrast stretching. It uses the same forumla as global contrast stretching, but the minimum and maximum values are calculated base on a 100x100 region surrounding each pixel.

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