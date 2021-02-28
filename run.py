import ahe
import clahe
import minmax
import quality

# ahe.ahe("testImages/groundTruths/eg1_lowcntrst.jpg")
# clahe.clahe("testImages/groundTruths/eg1_lowcntrst.jpg")
# minmax.minmax("testImages/groundTruths/eg1_lowcntrst.jpg")
# minmax.local_minmax("testImages/groundTruths/eg1_lowcntrst.jpg", 100)

print(quality.image_quality("testImages/groundTruths/eg1_lowcntrst.jpg", "testImages/groundTruths/eg1_grndtruth.jpg"))
# print(quality.image_quality("testImages/groundTruths/eg1_grndtruth.jpg", "testImages/groundTruths/eg1_grndtruth.jpg"))