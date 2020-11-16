from skimage.io import imread, imsave
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from scipy import ndimage
from sklearn.cluster import KMeans
import os
from kneed import KneeLocator
import time
from statistics import mean
# Scaling the image pixels values within 0-1

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
        image_2d = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

        #for saving image with different number of clusters as well as inertias for kmeans elbow method
        clustered_images = []
        inertias = []
        for i in range(2, 11): #num clusters
            kmeans = KMeans(n_clusters = i, random_state = 0).fit(image_2d)
            clustered = kmeans.cluster_centers_[kmeans.labels_]
            clustered_images.append(clustered)
            inertias.append(kmeans.inertia_)

        #populate KneeLocator from kneed with inertia data to locate ideal number of clusters using elbow method
        elbow_method_ideal_clusters = KneeLocator(
            range(2, 11), inertias, curve='convex', direction='decreasing'
        )

        #finds ideal num clusters ()
        elbow = elbow_method_ideal_clusters.elbow

        #plotting for saving elbow method plot for each image
        plotted, ax = plt.subplots()

        ax.plot(range(2, 11), inertias)
        plotted.savefig(os.path.join(OUTPUT_DATASET_DIR, filename + '_elbow_plot_' + str(elbow) + '.jpg'))


        print('elbow: ' + str(elbow))

        #save clustered image
        clustered = clustered_images[elbow - 2]
            
        clustered_3d = clustered.reshape(img.shape[0], img.shape[1], img.shape[2])

        clustered_3d = clustered_3d

        imsave(os.path.join(OUTPUT_DATASET_DIR, filename), clustered_3d)

        stop = time.perf_counter()

        print('time elapsed to cluster most recent image: ' + str(stop - start) + ' seconds')

        time_elapsed.append(stop - start)
    
    print('average time to cluster each image: ' + str(mean(time_elapsed)) + ' seconds')

    print('total time to cluster all images: ' + str(sum(time_elapsed)) + ' seconds')