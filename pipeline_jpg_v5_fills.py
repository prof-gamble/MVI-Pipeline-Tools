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
        if yside < xside:
            fills = 1
            xfills = xside
            imdelta = xside - yside
            yfills1 = int(imdelta / 2)
            yfilchk = 2 * yfills1
            if imdelta > yfilchk:
                yfills2 = yfills1 + 1
            else:
                yfills2 = yfills1
            topimage = np.zeros((yfills1,xfills,3), dtype = "uint8")
            bottomimage = np.zeros((yfills2,xfills,3), dtype = "uint8")
            imagesquare = cv2.vconcat([topimage, imagecrop, bottomimage])
        elif xside < yside:
            fills = 2
            yfills = yside
            imdelta = yside - xside
            xfills1 = int(imdelta / 2)
            xfilchk = 2 * xfills1
            if imdelta > xfilchk:
                xfills2 = xfills1 + 1
            else:
                xfills2 = xfills1
            rightimage = np.zeros((yfills,xfills1,3), dtype = "uint8")
            leftimage = np.zeros((yfills,xfills2,3), dtype = "uint8")
            imagesquare = cv2.hconcat([leftimage, imagecrop, rightimage])
        else:
            fills = 0
            imagesquare = imagecrop
        d = str(a)
        if not os.path.exists(objtag):
            os.makedirs(objtag)
        os.chdir(objtag)
        fovname = objtag + '_' + d + '_' + fnjpg
        cv2.imwrite(fovname, imagesquare)
        os.chdir('..')


# In[ ]:




