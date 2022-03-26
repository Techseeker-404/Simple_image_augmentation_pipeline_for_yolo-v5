import argparse
import sys
try:
    from augmentPipe import AugmentYoloData
except:
    from Augmenter.augmentPipe import AugmentYoloData
    
def main():
    parser = argparse.ArgumentParser(description="Plz pass arguments")
    parser.add_argument("-ipt", "--images_path", help="Path to images directory")
    parser.add_argument("-lpt", "--labels_path", help="Path to labels directory")
    parser.add_argument("-Aug", "--num_of_Aug", help="No.of Augmentations per image", default=5)

    args = parser.parse_args()

    AugData = AugmentYoloData(args.images_path, args.labels_path)
    AugData.augment(num_aug=int(args.num_of_Aug))

if __name__ == "__main__":
    sys.exit(main())
