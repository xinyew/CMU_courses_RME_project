import cv2
from pytesseract import pytesseract
from pytesseract import Output

cam = cv2.VideoCapture(0)

img_counter = 0
words = []

ret, frame = cam.read()
if not ret:
    print("failed to grab frame")

img_name = "opencv_frame_{}.png".format(img_counter)
cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))
img_counter += 1
img = cv2.imread(img_name)
(h, w) = img.shape[:2]
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, M, (w,h))
cv2.imwrite(img_name, rotated)

cam.release()

cv2.destroyAllWindows()

pytesseract.tesseract_cmd = "/bin/tesseract"
WINDOW_NAME = "win"

img = cv2.imread("opencv_frame_0.png")

imageData = pytesseract.image_to_data(img, output_type=Output.DICT)

for i, word in enumerate(imageData['text']):
    if word != "":
        x, y, w, h = imageData['left'][i], imageData['top'][i], imageData['width'][i], imageData['height'][i]
        cv2.putText(img, word, (x, y - 16), cv2.FONT_HERSHEY_COMPLEX, 0.5, (100, 100, 255), 1)
        print(word)
        nw = ''
        for le in word:
            if le == "'" or le == '"':
                continue
            nw += le
        words.append(nw)

cat = ""
for w in words:
    cat += w
    cat +=' '
url = "curl https://api.particle.io/v1/devices/e00fce68af794bddadf369e7/message -d arg='\n\n" + cat + "\n\n\n\n\n\n\n\n\n\n\n\n ' -d access_token=b2bc473484175c1f4f1f3bb864d9a633c9c05c45"
print()
print(cat)
print()
print(url)
print()

import os

stream = os.popen('echo Returned otput')

os.system(url)

output = stream.read()
