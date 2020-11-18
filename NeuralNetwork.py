import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras;
from tensorflow.keras import layers;
from tensorflow.keras.models import Sequential;

import time
from skimage.io import imread, imsave


IMAGE_DATASET_DIR = './ClusteredImages'

# OUTPUT_DATASET_DIR = './ClusteredNoFuelCapData'

if __name__ == "__main__":
    
    #
    batch_size = 32
    img_height = 180
    img_width = 180

    trainingDataset = tf.keras.preprocessing.image_dataset_from_directory(
        IMAGE_DATASET_DIR,
        validation_split=0.2,
        subset="training",
        seed=1,
        image_size=(img_height, img_width),
        batch_size=batch_size        
    )

    validationDataset = tf.keras.preprocessing.image_dataset_from_directory(
        IMAGE_DATASET_DIR,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    # can print the classe names with this
    class_names = trainingDataset.class_names

    # speeds up the i/o of reading and writing to files
    AUTOTUNE = tf.data.experimental.AUTOTUNE
    trainingDataset = trainingDataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    validationDataset = validationDataset.cache().prefetch(buffer_size=AUTOTUNE)

    num_classes = len(class_names)

    model = Sequential([
        layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        # layers.Conv2D(32, 3, padding='same', activation='relu'),
        # layers.MaxPooling2D(),
        # layers.Conv2D(64, 3, padding='same', activation='relu'),
        # layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
    ])

    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
        )

    model.summary()

    # train the model
    epochs = 25;
    history = model.fit(
        trainingDataset,
        validation_data = validationDataset,
        epochs = epochs
    )

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

