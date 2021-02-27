import ahe
import clahe
import minmax

ahe.ahe("testImages/groundTruths/eg1_lowcntrst.jpg")
clahe.clahe("testImages/groundTruths/eg1_lowcntrst.jpg")
minmax.minmax("testImages/groundTruths/eg1_lowcntrst.jpg")