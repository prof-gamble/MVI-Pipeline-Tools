Pipeline Image Extraction Tool (for MVI Modelers)

============================
Setting up Python:

4 Files
.pynb Files can be opened with Jupyter Notebook
.py files are Python files
pipeline_jpg_v2.pypipeline_jpg_v2.ipynbpipeline_png_v2.ipynbpipeline_png_v2.py

4 Library Modules are required:
import cv2
import os
import glob
import xml.etree.ElementTree as ET
cv2, os, and glob are separate from stdlib (so you may need to do a pip install of these)
Elementtree should be in stdlib.

1 other Library Module should be installed also:
To ensure the binding of the xml libraries, I also instal lxml (with pip)

============================
What the Program Does:
This program will process a dataset exported from MVI to create additional images using the object labels from images in that dataset.  The output is a subdirectory for each Object Label, inside of which user will find all occurrences of that object cropped to the bounding box with all original pixels. The files retain the original name preceded by the prefix of "object label_x_" (where x allows user to have multiples of an object type in the image).

For example, if a dataset has 100 images, each having 4 different objects, 4 object folders are created with 100 images in each folder.

This program can process user-defined bounding boxes, inferenced bounding boxes, and auto-labeled bounding boxes, including a mixed dataset of these types.

============================
Executing the Program:

(1) Determine the export image types: jpg or png
(2) Select the .py file needed based on the image types.
(3) Add the .py file to the same directory that the export images and their xml files reside.
(4) Run the python file from that same path or directory.

Pro Tip: On my PC, I made a shortcut key that opens a terminal window from any directory/folder that I have selected in Finder(Mac) or FileExplorer(Windows).

At the terminal window:  python pipeline_jpg_v2.py
It takes 5-20seconds to run depending on how many images.

=============================
Contact: egamble@us.ibm.com  for help.