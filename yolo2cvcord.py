import cv2
import matplotlib.pyplot as plt
import sys

args = sys.argv
img = cv2.imread(args[1])
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(840,720))
dh, dw, _ = img.shape

"""Reading label file"""
fl = open(args[2], 'r')
data = fl.readlines()
fl.close()

cord_lst = []

for dt in data:

    # Split string to float
    _, x, y, w, h = map(float, dt.split(' '))

    # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
    # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)
    
    if l < 0:
        l = 0
    if r > dw - 1:
        r = dw - 1
    if t < 0:
        t = 0
    if b > dh - 1:
        b = dh - 1
    cord_lst.append([l,t,r,b])
    print(l,t,r,b)
    cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 3)

print(cord_lst)
roi_img = img[192:252,285:440]
#roi_img = img[t:b,l:r]
cv2.imshow("roi_img",roi_img)

cv2.imshow("rec_img",img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
plt.imshow(img)
plt.show()
