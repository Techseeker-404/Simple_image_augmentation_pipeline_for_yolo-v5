#!/usr/bin/python3.8
import json

class_dict = {}
with open("YOLO_scanner/classes.txt") as f:
    content = f.readlines()
for num, elem in enumerate(content):
    class_dict[int(num)] = elem.strip()
#json_class = json.dumps(class_dict,indent=4)
json.dump(class_dict,open("YOLO_scanner/classes.json","w")) 
#check_json = json.load("YOLO_scanner/classes.json")
#print(check_json)
with open("YOLO_scanner/classes.json") as json_file:
    data = json.load(json_file)
print(data)
datas = json.load(open("YOLO_scanner/classes.json","r"))
print(datas)
