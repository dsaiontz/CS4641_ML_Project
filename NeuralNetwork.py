import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras;
from tensorflow.keras import layers;
from tensorflow.models import Sequential;


IMAGE_DATASET_DIR = './NoFuelCapTrainingSet'

OUTPUT_DATASET_DIR = './ClusteredNoFuelCapData'

if __name__ == "__main__":
    
    #make directory for clustered data, should it not exist already
    if not os.path.exists(OUTPUT_DATASET_DIR):
        os.makedirs(OUTPUT_DATASET_DIR)

    time_elapsed = [] #for metrics purpose, how long it took to cluster each image
    for filename in os.listdir(IMAGE_DATASET_DIR):
        start = time.perf_counter()
        print(filename)
        
        #reads image in and flattens it into 2d matrix
        img = imread(os.path.join(IMAGE_DATASET_DIR, filename))



    #
    trainingDataset = tf.keras.preprocessing.image_dataset_from_directory()