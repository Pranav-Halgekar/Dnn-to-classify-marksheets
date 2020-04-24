import os
import cv2
import keras
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

model = load_model('marksheet_classification.hdf5')

model.compile(optimizer ='adam', loss='categorical_crossentropy', metrics=['accuracy'])

path, dirs, files = next(os.walk("test_data"))
file_count = len(files)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

    except OSERROR:
            print('Error: Creating directory.'+directory)

            
createFolder('./classified data/')
createFolder('./classified data/')
createFolder('classified data/./campus alpha/')
createFolder('classified data/./campus beta/')
createFolder('classified data/./campus gamma/')
createFolder('classified data/./no campus/')
images=[]
results=[]

for i in range(0,file_count-1):
    imgpath="test_data/"+"application"+str(i)+".jpg"
    test_images= image.load_img(imgpath)
    test_image= image.load_img(imgpath,target_size=(64,64))
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    
    result=model.predict_classes(test_image)
    images.append(test_images)
    results.append(result)
    
print(results)
predictions=results
pred1=[]
path=os.getcwd()
for i in range(0,len(predictions)):
    if predictions[i]==0:
        pathalpha=path+"\campus alpha/"
        images[i].save(pathalpha+"application_"+str(i)+'.jpeg','JPEG')
        prediction='campus alpha'
        print(prediction)
        pred1.append(prediction)
    elif predictions[i]==1:
        pathbeta=path+"\campus beta/"
        images[i].save(pathbeta+"application_"+str(i)+'.jpeg','JPEG')

        prediction='campus beta'
        pred1.append(prediction)
        print(prediction)
    elif predictions[i]==2:
        pathgamma=path+"\campus gamma/"
        images[i].save(pathgamma+"application_"+str(i)+'.jpeg','JPEG')

        prediction='campus gamma'
        pred1.append(prediction)
        print(prediction)
    elif predictions[i]==3:
        pathno=path+"\no campus/"
        images[i].save(pathno+"application_"+str(i)+'.jpeg','JPEG')

        prediction='no campus'
        pred1.append(prediction)
        print(prediction)
    
    

