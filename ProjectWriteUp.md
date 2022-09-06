**Exploratory Data Analysis :**
tfrecord files divided into three train/val/test folders(80%/10%10%).
First part (bar plot) of additional EDA shows total number of objects in each frame.
Second part (pie chart) shows percentage of Cars, Bicycles and pedestrians in a random 10-frame dataset.
Third part [Reference of code of the last two cells : Udacity self-driving cars course] is the statistics analysis which calculates total
mean and variance for each color channel. Furthermore demonstrate Pixel value distribution per channel.


**Training / new_pipeline.config :**
first pipeline.config has been modified with no augmentation and no extra modification of the file. 
Results of the tensorboard and evaluation process clearly show modification of the process is required. The training loss is oscillating and does not reach a plateau. Increasing training dataset could help the process but still adding augmentations are required to mitigate results.
`tensorboard dev upload --logdir 'experiments/reference/pipline1'`
![alt text](https://github.com/PardisTaghavi/nd013-c1-vision-starter/blob/main/results/tensorboar_pip1.png)


**Model Improvment and Explore Augmentations:**
On the second round of training: augemntations are added to simulate blurriness, darkness, random occlusions and etc. This new config file has been trained again which shows improvement of the results [
`tensorboard dev upload --logdir 'experiments/reference/pipline2'` ]. However charts show convergence of loss functions for the same dataset and total loss decreased more iterations for training could help for reaching a plateau. 
![alt text](https://github.com/PardisTaghavi/nd013-c1-vision-starter/blob/main/results/tensorboard_pip2.png)


Augmentations are visualized in "Explore augmentations.ipynb". it should be noted that in the third round of training normalization is added to augmentations which result showing black images in Explore "augmentations.ipynb". This is due to the fact that normalization map all the pixel values to numbers between 0 and 1. I expected this model to perform the best, but total loss is slightly more than model 2, it does not show a great improvement in convergence or learning process. In this model more iterations are needed same as model 2. 
`tensorboard dev upload --logdir 'experiments/reference/pipline3'`
![alt text](https://github.com/PardisTaghavi/nd013-c1-vision-starter/blob/main/results/tensorboard_pip3.png)


Note1:  Considering exponential decay learning rate instead of cosine decay learning rate could be potentially investigated as well


Note2: creating animation for the first try showed multiple object detection for each object and many false detection as well which was not satisfying at all. Changing score_threshold of the non-maximum-supression to 0.65 in the config file improved results. 


(Following image is an example of model 2 with score_threshold of the non-maximum-supression=0.5)
![alt text](https://github.com/PardisTaghavi/nd013-c1-vision-starter/blob/main/results/config2Resault.png)

