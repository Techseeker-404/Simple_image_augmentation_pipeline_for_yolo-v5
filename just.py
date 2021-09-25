import ast
import os
import pandas as pd
import cv2
import numpy as np
import albumentations as Alb

df = pd.read_csv("yolo_object_detection.csv")

df.bbox_data = df.bbox_data.apply(ast.literal_eval)
count = 0
class_id = []
bboxes = []
for ind, row in df.iterrows():
    img_path = row["file_path"]
    print(img_path )
    data = row["bbox_data"]
    for i in range(len(data)):
    #    print(dt)
        class_no = data[i][0]
        class_id.append(class_no)
        bbox = data[i][1]
        bboxes.append(bbox)
        print(class_no, "&", bbox[0], bbox[1], bbox[2], bbox[3])
    break
    print("=======")
    count +=1
#print(count)
print(bboxes)
print(class_id)

image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
bboxParams = Alb.BboxParams(
        format='yolo', 
        label_fields=['class_id']
)
transform = Alb.Compose([
    Alb.RandomSizedBBoxSafeCrop(
        width=1024, height=1024, 
        erosion_rate=0.2
    )],
    bbox_params = bboxParams
)


transformed = transform(
        image=image, 
        bboxes=bboxes, 
        class_id=class_id
)
#print(transformed["image"],list(transformed['bboxes']),transformed["class_id"])
print(transformed['bboxes'])
print(transformed["class_id"])
savlst = []
for i,tup in enumerate(transformed["bboxes"]):
    savlst.append([
        int(transformed["class_id"][i]),
        tup[0], tup[1], tup[2], tup[3]
    ])
print(savlst)
sav_arr = np.array(savlst)
print(sav_arr)
np.savetxt(
    "just.txt",
    sav_arr,
    fmt = ["%d","%f","%f","%f","%f"],
)
new_image = transformed["image"]
new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
cv2.imwrite("just.jpg",new_image)
if os.path.isfile("just.jpg"):
    print("File Created.")
