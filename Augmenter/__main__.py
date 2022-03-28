import argparse
import sys
import os
try:
    from augmentPipe import AugmentYoloData
except:
    from Augmenter.augmentPipe import AugmentYoloData

def split_test_train(split_test_perc):
    TRAIN_IMG = "augmented/images/train"
    TEST_IMG = "augmented/images/test"
    TRAIN_LBL = "augmented/labels/train"
    TEST_LBL = "augmented/labels/test"

    #*Lambda function to make direcrtory*#
    make_dir = lambda dir_name : os.makedirs(dir_name, exist_ok=True)
    
    IMAGES = "augmented/images/"
    LABELS = "augmented/labels/"
    image_lst = os.listdir(IMAGES)
    label_lst = os.listdir(LABELS)
    TEST_PERC = int(len(image_lst) * (int(split_test_perc) / 100))
    test_img_lst = image_lst[ :TEST_PERC]
    train_img_lst = image_lst[TEST_PERC: ]
    test_label_lst = label_lst[ :TEST_PERC]
    train_label_lst = label_lst[TEST_PERC:]
    #*For images*#
    make_dir(TEST_IMG)
    #print(test_img_lst)
    [os.replace(f"{IMAGES}/{i}",f"{TEST_IMG}/{i}") for i in test_img_lst]
    make_dir(TRAIN_IMG)
    [os.replace(f"{IMAGES}/{i}",f"{TRAIN_IMG}/{i}") for i in train_img_lst]
    
    #*For Labels*#
    make_dir(TEST_LBL)
    #print(test_label_lst)
    [os.replace(f"{LABELS}/{i}",f"{TEST_LBL}/{i}") for i in test_label_lst]
    make_dir(TRAIN_LBL)
    [os.replace(f"{LABELS}/{i}",f"{TRAIN_LBL}/{i}") for i in train_label_lst]

    
def main():
    parser = argparse.ArgumentParser(description="Plz pass arguments")
    parser.add_argument("-ipt", "--images_path", help="Path to images directory")
    parser.add_argument("-lpt", "--labels_path", help="Path to labels directory")
    parser.add_argument("-Aug", "--num_of_Aug", help="No.of Augmentations per image", default=5)
    parser.add_argument(
        "-spt", "--split_test_percntg",
        help="Split dataset into train and test with given number as % of file",
        default=None
    )
    args = parser.parse_args()

    AugData = AugmentYoloData(args.images_path, args.labels_path)
    AugData.augment(num_aug=int(args.num_of_Aug))

    #** Train and Test Split**#
    if args.split_test_percntg != None:
        print("Just Hold on for a while ...")
        split_test_train(int(args.split_test_percntg))


if __name__ == "__main__":
    sys.exit(main())
