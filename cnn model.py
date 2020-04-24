from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import regularizers
import os
#initialising cnn
classifier= Sequential()

# convolution layer and maxpooling
classifier.add(Convolution2D(32,3,3, input_shape =(128,128,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(64,3,3, activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(128,3,3, activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(256,3,3, activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
#flattening
classifier.add(Flatten())


#full connection
classifier.add(Dense(output_dim= 128,kernel_regularizer=regularizers.l2(3), activation='relu'))
classifier.add(Dense(output_dim= 128,kernel_regularizer=regularizers.l2(2), activation='relu'))
classifier.add(Dense(output_dim= 128,kernel_regularizer=regularizers.l2(1), activation='relu'))
classifier.add(Dense(output_dim= 128,kernel_regularizer=regularizers.l2(0.01), activation='relu'))

classifier.add(Dense(output_dim= 4, activation='softmax'))

#compiling
classifier.compile(optimizer ='adam', loss='categorical_crossentropy', metrics=['accuracy'])




#fitting
address=os.getcwd()


path=os.getcwd()
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        vertical_flip= True)

test_datagen = ImageDataGenerator(rescale=1./255)

pathtrain=path.__add__('\\training_set')
train_generator = train_datagen.flow_from_directory(
        pathtrain,# enter working directory address for training_set
        target_size=(128,128),
        batch_size=32,
        class_mode='categorical')
pathtest=path+"\\test_set"
validation_generator = test_datagen.flow_from_directory(
        pathtest,# enter working directory address for test_set
        target_size=(128,128),
        batch_size=32,
        class_mode='categorical')

classifier.fit_generator(
        train_generator,
        steps_per_epoch=53,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=25)


#saving model

classifier.save("marksheet_classification.hdf5")