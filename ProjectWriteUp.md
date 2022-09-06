**Exploratory Data Analysis :**
tfrecord files divided into three train/val/test folders(80%/10%10%).
First part (bar plot) of additional EDA shows total number of objects in each frame.
Second part (pie chart) shows percentage of Cars, Bicycles and pedestrians in a random 10-frame dataset.
Third part [Reference of code of the last two cells : Udacity self-driving cars course] is the statistics analysis which calculates total
mean and variance for each color channel. Furthermore demonstrate Pixel value distribution per channel.


**Training / new_pipeline.config :**
first pipeline.config has been modified with no augmentation and no extra modification of the file. 
Results of the tensorboard and evaluation process clearly show modification of the process is required.
`tensorboard dev upload --logdir 'experiments/reference/pipline1'`

**Model Improvment and Explore Augmentations:**
On the second round of training: augemntations are added to simulate blurriness, darkness, random occlusions and etc. This new config file has been trained again which shows improvement of the results [
`tensorboard dev upload --logdir 'experiments/reference/pipline2'` ].

Augmentations are visualized in "Explore augmentations.ipynb". it should be noted that in the third round of training normalization is added to augmentations which result showing black images in Explore "augmentations.ipynb". This is due to the fact that normalization map all the pixel values to numbers between 0 and 1.
`tensorboard dev upload --logdir 'experiments/reference/pipline3'`

Note1: Final esults of the three config different config files with tensorboard can be found in the Resauls directory.
Note2: creating animation for the first try showed multiple object detection for each object and many fault detection as well which was not satisfying at all. Changing score_threshold of the non-maximum-supression to 0.6 in the config file improved results.
