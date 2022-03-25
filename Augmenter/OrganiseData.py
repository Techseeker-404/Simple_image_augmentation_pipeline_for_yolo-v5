import ast
import re
import os
import argparse
import pandas as pd


class OrganiseYoloData:
    def __init__(self, imagesPath, labelsPath):
        self.imagesPath = imagesPath
        self.labelsPath = labelsPath

    def create_dataframe(self, save_file=None):
        df = pd.DataFrame()
        for image_file in os.listdir(self.imagesPath):
            print(image_file)
            image_file_name, exten = os.path.splitext(image_file)
            file_dict = {}
            lines = []
            print(image_file_name)
            for text_file in os.listdir(self.labelsPath):
                text_file_name, exten = text_file.split(".")

                if image_file_name == text_file_name:
                    with open(os.path.join(self.labelsPath,text_file)) as f:
                        #contents = f.read()
                        lines = f.readlines()
                file_dict["file_path"] = os.path.join(self.imagesPath, image_file)
                file_dict["bbox_data"] = [lines]
            df_set = pd.DataFrame(file_dict,index=[0])
            df = df.append(df_set,ignore_index=True)
            print(file_dict)
        print(df.head(3))
        if save_file != None:
            df.to_csv(save_file)
        rand_data = df.loc[2,"bbox_data"]
        print(rand_data)
        return df

    def get_class_bbox(self,colmns, from_csv=True):
        if from_csv == False:
            check_lst = colmns
        else:
            check_lst = ast.literal_eval(colmns)
        print(len(check_lst))
        datas = pd.DataFrame()
        class_lst = []
        for cls in range(len(check_lst)):
            class_no = int(check_lst[cls][:2])
            bbox_list = check_lst[cls][2:]
            new_data = re.sub("[^0-9-.]", " ",bbox_list)
            bbox_list = re.findall("\d+\.\d+",new_data)
            bbox_list = [float(i) for i in bbox_list]
            class_tup = (class_no,bbox_list)
            class_lst.append(class_tup)
        #print(class_lst)    
        return class_lst

    def create_organiseData(self,file_name="yolo_train.csv",csv=False, save_file=False):
        datas = pd.DataFrame()
        dataframe = self.create_dataframe()
        for ind, row in dataframe.iterrows():
            #print(row["file_path"], row["bbox_data"])
            files_dict = {}
            if csv == False:
                col_lst = self.get_class_bbox(row["bbox_data"],from_csv=False)
            else:
                col_lst = self.get_class_bbox(row["bbox_data"])
            files_dict["file_path"] = row["file_path"]
            files_dict["bbox_data"] = [col_lst]
            df_set = pd.DataFrame(files_dict)
            datas = datas.append(df_set,ignore_index=True)
            print(files_dict)
        #print(datas)
        if save_file == True:
            datas.to_csv(file_name)
        return datas

if __name__ == "__main__":
    #images_path = "../YOLO_scanner/images/"
    #labels_path = "../YOLO_scanner/labels/"
    parser = argparse.ArgumentParser(description="Plz pass arguments")
    parser.add_argument("-ip", "--images_path", help="Path to images directory")
    parser.add_argument("-lp", "--labels_path", help="Path to labels directory")

    args = parser.parse_args()

    DataOrg = OrganiseYoloData(args.images_path, args.labels_path)
    #DataOrg.create_dataframe()
    DataOrg.create_organiseData(file_name="yolo_object_detection.csv", save_file=True)
