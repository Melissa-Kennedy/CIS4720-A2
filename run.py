import ahe
import clahe
import minmax
import quality

ahe.ahe("testImages/groundTruths/eg1_lowcntrst.jpg")
clahe.clahe("testImages/groundTruths/eg1_lowcntrst.jpg")
minmax.minmax("testImages/groundTruths/eg1_lowcntrst.jpg")
minmax.local_minmax("testImages/groundTruths/eg1_lowcntrst.jpg", 100)

base_quality = quality.image_quality("testImages/groundTruths/eg1_lowcntrst.jpg", "testImages/groundTruths/eg1_grndtruth.jpg")
ahe_quality = quality.image_quality("editedImages/adaptive_histogram_equalization.jpg", "testImages/groundTruths/eg1_grndtruth.jpg")
clahe_quality = quality.image_quality("editedImages/contrast_limited_adaptive_histogram_equalization.jpg", "testImages/groundTruths/eg1_grndtruth.jpg")
minmax_quality = quality.image_quality("editedImages/minmax.jpg", "testImages/groundTruths/eg1_grndtruth.jpg")
minmax_local_quality = quality.image_quality("editedImages/local_minmax.jpg", "testImages/groundTruths/eg1_grndtruth.jpg")

print(f"Base Image Quality: {base_quality}")
print(f"AHE Image Quality: {ahe_quality}")
print(f"CLAHE Image Quality: {clahe_quality}")
print(f"MinMax Image Quality: {minmax_quality}")
print(f"Local MinMax Image Quality: {minmax_local_quality}")
# print(quality.image_quality("testImages/groundTruths/eg1_grndtruth.jpg", "testImages/groundTruths/eg1_grndtruth.jpg"))