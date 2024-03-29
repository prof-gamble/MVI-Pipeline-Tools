#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import glob
import xml.etree.ElementTree as ET
import numpy as np


# In[3]:


parent_dir = os.getcwd()


# In[4]:


xmlfiles = glob.glob('*.xml')


# In[5]:


for fnxml in xmlfiles:
    fntemp = fnxml
    fn = fntemp[:-4]
    fnjpg = fn + '.jpg'
    image = cv2.imread(fnjpg)
    tree = ET.parse(fnxml)
    root = tree.getroot()
    a = 0
    for bbox in root.findall('object'):
        a = a + 1
        objtag = (root[a][1].text)
        if objtag == "1":
            decchk = "."
        else:
            decchk = objtag[1] 
        if decchk == ".":
            b = 2
            c = 3
        else:
            b = 1
            c = 2    
        objtag = (root[a][b].text)
        xminbox = int(root[a][c][0].text)
        yminbox = int(root[a][c][1].text)
        xmaxbox = int(root[a][c][2].text)
        ymaxbox = int(root[a][c][3].text)
        xphotomax = int(root[0][0].text)
        yphotomax = int(root[0][1].text)
        if xmaxbox <= xphotomax:
            xstop = xmaxbox
        else:
            xstop = xphotomax
        xside = xstop - xminbox
        if ymaxbox <= yphotomax:
            ystop = ymaxbox
        else:
            ystop = yphotomax
        yside = ystop - yminbox
        imagecrop = image[yminbox:ystop, xminbox:xstop]
        d = str(a)
        if not os.path.exists(objtag):
            os.makedirs(objtag)
        os.chdir(objtag)
        fovname = objtag + '_' + d + '_' + fnjpg
        cv2.imwrite(fovname, imagecrop)
        os.chdir('..')

# In[ ]:




