
def recognize(filepath):
    return "M"

def isCorrect(sex, filepath):
    if filepath[4]==sex:
        return True
    return False

if __name__=="__main__":
    files=[
        "001_K.wav",    "020_M.wav",    "039_M.wav",    "058_M.wav",    "077_K.wav",
        "002_M.wav",   "021_M.wav",    "040_K.wav",    "059_K.wav",    "078_M.wav",
        "003_K.wav",    "022_K.wav",    "041_K.wav",    "060_K.wav",    "079_K.wav",
        "004_M.wav",    "023_M.wav",    "042_M.wav",    "061_M.wav",    "080_M.wav",
        "005_M.wav",    "024_M.wav",    "043_M.wav",    "062_K.wav",    "081_K.wav",
        "006_K.wav",    "025_K.wav",    "044_K.wav",    "063_M.wav",    "082_M.wav",
        "007_M.wav",    "026_M.wav",    "045_M.wav",    "064_M.wav",    "083_K.wav",
        "008_K.wav",    "027_M.wav",    "046_K.wav",    "065_M.wav",    "084_M.wav",
        "009_K.wav",    "028_K.wav",    "047_K.wav",    "066_K.wav",    "085_K.wav",
        "010_M.wav",    "029_K.wav",    "048_K.wav",    "067_K.wav",    "086_K.wav",
        "011_M.wav",    "030_M.wav",    "049_M.wav",    "068_K.wav",    "087_M.wav",
        "012_K.wav",    "031_K.wav",    "050_K.wav",    "069_K.wav",    "088_K.wav",
        "013_M.wav",    "032_M.wav",    "051_K.wav",    "070_M.wav",    "089_M.wav",
        "014_K.wav",    "033_M.wav",    "052_M.wav",    "071_M.wav",    "090_M.wav",
        "015_K.wav",    "034_K.wav",    "053_M.wav",    "072_K.wav",    "091_M.wav",
        "016_K.wav",   "035_M.wav",    "054_K.wav",    "073_K.wav",
        "017_M.wav",   "036_K.wav",    "055_K.wav",    "074_K.wav",
        "018_K.wav",    "037_K.wav",    "056_M.wav",   "075_M.wav",
        "019_M.wav",   "038_M.wav",    "057_K.wav",    "076_M.wav",
    ]
    result=0;
    for i in range(len(files)):
        if isCorrect(recognize(files[i]), files[i]):
            result+=1
    print(result/len(files))
