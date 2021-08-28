import cv2
import sys
from docExtractor import DocFromID

args = sys.argv

img = cv2.imread(args[1])
img = cv2.resize(img, (820,640))
roi = cv2.selectROI(img)

print(roi)

img_crop = img[
        int(roi[1]):int(roi[1]+roi[3]) ,
        int(roi[0]):int(roi[0]+roi[2])
    ]
cv2.imshow("cropped_section", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Extracting data...")
docs = DocFromID(img_crop, cv_image=True)
print(docs.get_text())
if cv2.waitKey(1) & 0xFF == ord("q"):
    exit

