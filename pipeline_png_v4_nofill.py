#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import glob
import xml.etree.ElementTree as ET


# In[2]:


parent_dir = os.getcwd()


# In[3]:


xmlfiles = glob.glob('*.xml')


# In[9]:


for fnxml in xmlfiles:
    fntemp = fnxml
    fn = fntemp[:-4]
    fnpng = fn + '.png'
    image = cv2.imread(fnpng)
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
        imagecrop = image[yminbox:ymaxbox, xminbox:xmaxbox]
        d = str(a)
        if not os.path.exists(objtag):
            os.makedirs(objtag)
        os.chdir(objtag)
        fovname = objtag + '_' + d + '_' + fnpng
        cv2.imwrite(fovname, imagecrop)
        os.chdir('..')


# In[ ]:




