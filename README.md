# Dnn-to-classify-marksheets
Dnn to classify marksheets
>> Manual to run the programs

1. Software requirements
>> programs need python programming software(any version above 3.6)
>> spyder3
>> following libraries should be installed:
	1. pandas
	2. numpy
	3. keras
	4. tensorflow
	5. opencv
	6. pyqt5
	7. os
2. Folder structure
>> The folder named Final contains two subfolders
	1. Dnn application
	2. Dnn model
>> The Dnn model folder contains two folders
	1. Training_set
	2. Test_set
training and test set folders further contain four classification folders:Campus alpha, campus beta, campus gamma, no campus.

3. Running Cnn model
>> images of marksheets are to be splited into respective folders in training set and test set. 
>> run  the renaming code available in each folder.
>> double click on cnn model.py file to generate a model marksheet_classification.hdf5 
>> if required make changes to code in cnnmodel.py


4. Classifying marksheets
>> save the marksheet_classification.hdf5 in dnn application folder
>> add images to the test_data folder and run  the renaming code
>> run  the classification file.py. This generates four folders containing classified images



5. Errors
>> Any errors that may arise are due to issues with the working directory.

Note that the current saved model is trained on a dataset containing very less images and therefore has a training accuracy of 78% and a validation accuracy of 56%. 
To increase accuracy please use datasets with large number of images.
