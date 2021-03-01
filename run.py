import ahe
import clahe
import minmax
import quality
from os import path

def main():
    prefix = input("Enter file prefix: ")
    number = input("Enter number (0 for empty): ")
    number = "" if int(number) == 0 else str(number)

    if not path.exists(f"testImages/{prefix}_lowcntrst{number}.jpg"):
        return
        
    algo = input("Enter algorithm name (CLAHE, AHE, minmax, local, all): ")

    if algo.lower() == "ahe":
        ahe.ahe(f"testImages/{prefix}_lowcntrst{number}.jpg")

        base_quality = quality.image_quality(f"testImages/{prefix}_lowcntrst{number}.jpg", f"testImages/{prefix}_grndtruth.jpg")
        ahe_quality = quality.image_quality(f"editedImages/adaptive_histogram_equalization.jpg", f"testImages/{prefix}_grndtruth.jpg")
        
        print(f"Base Image Quality: {base_quality}")
        print(f"AHE Image Quality: {ahe_quality}")
    elif algo.lower() == "clahe":
        clahe.clahe(f"testImages/{prefix}_lowcntrst{number}.jpg")
        
        base_quality = quality.image_quality(f"testImages/{prefix}_lowcntrst{number}.jpg", f"testImages/{prefix}_grndtruth.jpg")
        clahe_quality = quality.image_quality(f"editedImages/contrast_limited_adaptive_histogram_equalization.jpg", f"testImages/{prefix}_grndtruth.jpg")
        
        print(f"Base Image Quality: {base_quality}")
        print(f"CLAHE Image Quality: {clahe_quality}")
    elif algo.lower() == "minmax":
        minmax.minmax(f"testImages/{prefix}_lowcntrst{number}.jpg")
        
        base_quality = quality.image_quality(f"testImages/{prefix}_lowcntrst{number}.jpg", f"testImages/{prefix}_grndtruth.jpg")
        minmax_quality = quality.image_quality(f"editedImages/minmax.jpg", f"testImages/{prefix}_grndtruth.jpg")
        
        print(f"Base Image Quality: {base_quality}")
        print(f"MinMax Image Quality: {minmax_quality}")
    elif algo.lower() == "local":
        minmax.local_minmax(f"testImages/{prefix}_lowcntrst{number}.jpg", 50)
        
        base_quality = quality.image_quality(f"testImages/{prefix}_lowcntrst{number}.jpg", f"testImages/{prefix}_grndtruth.jpg")
        minmax_local_quality = quality.image_quality(f"editedImages/local_minmax.jpg", f"testImages/{prefix}_grndtruth.jpg")
        
        print(f"Base Image Quality: {base_quality}")
        print(f"Local MinMax Image Quality: {minmax_local_quality}")
    elif algo.lower() == "all":
        ahe.ahe(f"testImages/{prefix}_lowcntrst{number}.jpg")
        clahe.clahe(f"testImages/{prefix}_lowcntrst{number}.jpg")
        minmax.minmax(f"testImages/{prefix}_lowcntrst{number}.jpg")
        minmax.local_minmax(f"testImages/{prefix}_lowcntrst{number}.jpg", 50)

        base_quality = quality.image_quality(f"testImages/{prefix}_lowcntrst{number}.jpg", f"testImages/{prefix}_grndtruth.jpg")
        ahe_quality = quality.image_quality(f"editedImages/adaptive_histogram_equalization.jpg", f"testImages/{prefix}_grndtruth.jpg")
        clahe_quality = quality.image_quality(f"editedImages/contrast_limited_adaptive_histogram_equalization.jpg", f"testImages/{prefix}_grndtruth.jpg")
        minmax_quality = quality.image_quality(f"editedImages/minmax.jpg", f"testImages/{prefix}_grndtruth.jpg")
        minmax_local_quality = quality.image_quality(f"editedImages/local_minmax.jpg", f"testImages/{prefix}_grndtruth.jpg")

        print(f"Base Image Quality: {base_quality}")
        print(f"AHE Image Quality: {ahe_quality}")
        print(f"CLAHE Image Quality: {clahe_quality}")
        print(f"MinMax Image Quality: {minmax_quality}")
        print(f"Local MinMax Image Quality: {minmax_local_quality}")
    else:
        print("not valid")
        return

if __name__ == "__main__":
    main()