#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤：
# 步骤1：对存储文件夹处理：将卷名称作为文件夹名，如：1,2,100,130.(对应代码：step1)
#*****************************************************************************
import os
import sys
import json
import random
import image 
from PIL import Image

#*********************************founctions*************************************
def main():
    path = '/media/xian/tripitaka/ZC/ZC_DATA'
    folders = os.listdir(path)
    for folder in folders:
        oldFolder = os.path.join(path,folder)
        newFolder = os.path.join(path,str(int(folder)))
        os.rename(oldFolder,newFolder)
if __name__ == '__main__':
    main()