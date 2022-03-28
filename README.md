### <ins> Image annotation and Augmentation. </ins>

#### To prepare a dataset of YOLO specification we used "LabelImg tool" 
##### installation steps and usage are mentioned in their repo itself.https://github.com/tzutalin/labelImg

#### Using labelimg we can annotate the existing data sets based on the data classes that we need to be detected by bounding boxes .The corresponding label of an image will be generated as a .txt file containing all data classes and its yolo formatted "bbox cordinates"
#### Yolo expects data in certain format that images need to be stored in `images` directory and labels needs to stored in `labels` directory .

#### <ins> Augmentation </ins>

##### If the image dataset we annotated is tad less for training any state of the art model. We need to augment that images to some trainable amount of images (Using this library a dataset can be augmented to any further number of images).

#####    This Library was created for the above mentioned purpose.Which sits on top of the "Albumentations " library. Here apart from augmenting images the bounding box data will also be preserved . 

#### NB:- Need Albumentations>=1.0.3 

#### Once we have images in `images` folder and labels in `labels` folder we can augment images by     running command `python3.8 Augmenter -ipt <images-path> -lpt <labels-path>` on terminal which will create augmented images and labels in a folder called `augmented` , Also number of augmentaions per image can be passed as argument `-Aug <number>`. If the class is imported on a python file we can add or further change transformations as well.

#### To split dataset into train-test set just pass argument "-spt alongside percentage of test set required". i.e `-spt 20` for creating a test set out of 20% of total files.

#### Also there is provision to created a .csv file which contains all images path and data classes of that images with its bboxes . It will comes in handy to keep track of image dataset and also needs to convert it into any other format.
#### For additional CLI help, executing command  `python3.8 Augmenter --help or -h` on terminal will provide CLI instructions.
##### ```$ tree augmented```
```
augmented
├── images
└── labels
```

