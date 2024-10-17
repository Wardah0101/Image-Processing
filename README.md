
# Bacteria Colony Detection
This project processes an image of a bacteria colony, applies various image processing techniques, and detects black spots within the colony using OpenCV and Python.

## Project Overview
The code performs the following tasks:

#### Read and Display Image: 
Loads a bacteria colony image and displays the original and grayscale versions.
#### Apply Gaussian Blur: 
Reduces noise in the grayscale image using a Gaussian blur.
#### Display Histogram:
Plots the histogram of the blurred image to analyze pixel intensity distribution.
#### Spot Detection:
Creates a mask to detect dark spots in the colony and then finds the contours of these spots.
#### Highlight Spots:
Colors the detected spots and overlays them on the original image.

## Libraries Used
* OpenCV
* NumPy
* Matplotlib


## How to Run
#### 1. Clone the repository:

`git clone https://github.com/Wardah0101/Image-Processing.git`
#### 2. Install the required dependencies:

`pip install opencv-python numpy matplotlib`




