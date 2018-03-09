#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤：
# 步骤2：对图片名进行格式化，全部修改为：数字+后缀。便于后面统一操作。
#（注意，这里有两个地方需要手动调整：1、main方法中藏经文件夹路径；2、renameFile方法中命名规则）
#*****************************************************************************
import os
import sys
import json
import random
import image 
from PIL import Image

FILETYPES = ['.jpg','.tiff','.png']
#*********************************founctions*************************************
#遍历文件夹，获取所有文件路径
def myEachFiles(path):
    _pathList=[]
    filepath = path
    fileTypes = FILETYPES
    if os.path.isdir(filepath):
        pathDir =  os.listdir(filepath)
        for allDir in pathDir:
            
            child = os.path.join('%s/%s' % (filepath, allDir))
            if os.path.isdir(child):
                _pathList.append(myEachFiles(child))
                pass
            else:
                typeList = os.path.splitext(child)
                if typeList[1] in fileTypes:#check file type:.txt
                    _pathList.append(child)
                    #print('child:','%s' % child.encode('utf-8','ignore'))
                    pass
                else:#not .txt
                    pass
            
        pass
    else:
        typeList = os.path.splitext(filepath)
        if typeList[1] in fileTypes:#check file type:.txt
            _pathList.append(filepath)
            pass    
        
        
        #print ('---',child.decode('cp936') )# .decode('gbk')是解决中文显示乱码问题
    return _pathList

#整理txt文件路径，统一放到一个列表当中，便于使用
def getFilePath(pathList):
    txtPathList = []
    fileTypes = FILETYPES
    for index in pathList:
        if type(index) is list:
            for item in getFilePath(index):
                typeList = os.path.splitext(item)
                if typeList[1] in fileTypes:#check file type:.txt
                    txtPathList.append(item)
                
            
            pass  
        else:
            typeList = os.path.splitext(index)
            if typeList[1] in fileTypes:#check file type:.txt
                txtPathList.append(index)
                pass
    return txtPathList
#rename
def renameFile(path):
    # read files
    pathList = myEachFiles(path)
    files = getFilePath(pathList)
    dic={}
    
    # rename file
    for file in files:
        (filepath,tempfilename) = os.path.split(file);  
        (shortname,extension) = os.path.splitext(tempfilename); 
        #命名规则
        # names = ['001','002','003','004','005','006','007']
        # if shortname in names:
        #     newname = str(int(shortname))#用来对图片重命名，根据不同藏经的规律，手动调整。
        # else:
        #     newname = str(int(shortname)+7)
        if '-' in shortname:
            newname = shortname.replace('-','')
        dst = os.path.join(filepath,newname+extension)
        try:
            os.rename(file, dst)
        except IOError as e:
            print('rename error:',e)
            pass

def main():
    #藏经文件夹路径,手动调整
    path = '/media/xian/tripitaka/QS/QS_DATA/69'
    #重命名
    renameFile(path)

if __name__ == '__main__':
    main()