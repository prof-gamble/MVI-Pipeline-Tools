#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import xml.etree.ElementTree as ET
import shutil


# In[6]:


parentdirectory = os.getcwd()
newdirectory = os.path.basename(parentdirectory)


# In[11]:


if not os.path.exists(newdirectory):
    os.mkdir(newdirectory)
else:
    shutil.rmtree(newdirectory)
    os.mkdir(newdirectory)
os.chdir(parentdirectory)


# In[12]:


os.chdir(newdirectory)
writepath = os.getcwd() + '/prop.json'
zippydir = os.getcwd()
os.chdir(parentdirectory)
readpath = os.getcwd() + '/prop.json'
shutil.copyfile(readpath, writepath)


# In[13]:


oldlabel = input('Original Label Name: ')
newlabel = input('New/Re-label Name: ')


# In[14]:


xmlfiles = glob.glob('*.xml')
nopic = 0


# In[15]:


for fnxml in xmlfiles:
    fntemp = fnxml
    fn = fntemp[:-4]
    fnjpg = fn + '.jpg'
    fnpng = fn + '.png'
    readjpg = parentdirectory + '/' + fnjpg
    writejpg = parentdirectory + '/' + newdirectory + '/' + fnjpg
    readpng = parentdirectory + '/' + fnpng
    writepng = parentdirectory + '/' + newdirectory + '/' + fnpng
    if os.path.isfile(fnjpg):
        shutil.copyfile(readjpg, writejpg)
    elif os.path.isfile(fnpng):
        shutil.copyfile(readpng, writepng)
    else:
        nopic = nopic + 1
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
            if root[a][2].text == oldlabel:
                root[a][2].text = newlabel
        else:
            if root[a][1].text == oldlabel:
                root[a][1].text = newlabel               
    os.chdir(newdirectory)
    tree.write(fnxml)
    os.chdir('..')


# In[16]:


shutil.make_archive(newdirectory, 'zip', zippydir)


# In[ ]:




