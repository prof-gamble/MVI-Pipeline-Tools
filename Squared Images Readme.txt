
Pipeline Image Extraction Tool (for MVI Modelers)

Squared Image Program

============================

This version of the Pipeline Image Extraction Tool will exactly match what occurs inside the iOS App. 
Rectangular bounding boxes are converted to exact squares, by pixel count, through the addition of black fill symmetrically applied to center the image in a square.

============================

Setting up Python:

4 Files
.pynb Files can be opened with Jupyter Notebook
.py files are Python files
pipeline_jpg_v3.pypipeline_jpg_v3.ipynbpipeline_png_v3.ipynbpipeline_png_v3.py

5 Library Modules are required:
import cv2
import os
import glob
import xml.etree.ElementTree as ET
Import numpy as np
cv2, os, numpy, and glob are separate from stdlib (so you may need to do a pip install of these)
Elementtree should be in stdlib.

1 other Library Module should be installed also:
To ensure the binding of the xml libraries, I also instal lxml (with pip)

=============================
Contact: egamble@us.ibm.com  for help.