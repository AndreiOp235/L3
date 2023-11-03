# L3
Simple lane Detector using python 3.6 and openCV

A step by step approach is used, From a shrunk down grayscale image, we get a top-down view of only the road (hard-coded). With the help of a sobel filter we extract the edge of the lane and extrapolate the first order equation that best passes through it. 
Such line is then overlayed over the image
