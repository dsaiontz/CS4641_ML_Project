# CS4641_ML_Project


# Summary Figure

# Introduction
We plan on combining both ML and Computer Vision techniques to identify the fuel cap on a vehicle.  As autonomous vehicles become increasingly common, we expect that people will want their cars to be able refuel themselves autonomously.  To facilitate this, we seek to develop an algorithm which can identify the fuel caps on vehicles.  This algorithm could then be used to pilot a robotic arm which could handle the refueling process.  

As far as we can tell, this algorithm has not been implemented.

We hope to develop an algorithm which is successful more than 99% of the time in identifying the fuel port within a picture of a car when the fuel port is fully within the picture.  We believe that the development of such an algorithm is important step in achieving the autonomous refueling of vehicles.  

# Methods and Dataset

Our dataset will consist of images of fuel caps/fuel doors on vehicles, as well as pictures where the vehicle is far away/a fuel cap is not visible. These images will be scraped from the Internet, and then we will split them between images with a visible fuel cap and ones without a visible fuel cap.

Our unsupervised portion will combine computer vision and clustering algorithms to define "shapes" visible in the imagee, or prominent features of images. These clusters will be created by identifying lines in the image with computer vision and creating clusters using these lines.

Our supervised portion will utilize a trained neural network to then identify, once these clusters are generated, to identify whether or not a fuel cap is visible.

# Results 

# Discussion

# References
