#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤：
# 步骤8：对原图片进行打包，存储到ZIP文件夹。
#（注意，这里有两个地方需要手动调整（main方法中）：1、要处理的藏经文件夹路径path；2、处理后的压缩包存储路径zip_path。）
#*****************************************************************************
import os
import sys
import json
import random
import image 
from PIL import Image
import zipfile
#*********************************founctions*************************************
def zip_dir(dirname,zipfilename):
    """
    | ##@函数目的: 压缩指定目录为zip文件
    | ##@参数说明：dirname为指定的目录，zipfilename为压缩后的zip文件路径
    | ##@返回值：无
    | ##@函数逻辑：
    """
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
 
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
class ZFile(object):   
    def __init__(self, filename, mode='r', basedir=''):   
        self.filename = filename   
        self.mode = mode   
        if self.mode in ('w', 'a'):   
            self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)   
        else:   
            self.zfile = zipfile.ZipFile(filename, self.mode)   
        self.basedir = basedir   
        if not self.basedir:   
            self.basedir = os.path.dirname(filename)   
          
    def addfile(self, path, arcname=None):   
        path = path.replace('//', '/')   
        if not arcname:   
            if path.startswith(self.basedir):   
                arcname = path[len(self.basedir):]   
            else:   
                arcname = ''   
        self.zfile.write(path, arcname)   
              
    def addfiles(self, paths):   
        for path in paths:   
            if isinstance(path, tuple):   
                self.addfile(*path)   
            else:   
                self.addfile(path)   
              
    def close(self):   
        self.zfile.close()   
          
    def extract_to(self, path):   
        for p in self.zfile.namelist():   
            self.extract(p, path)   
              
    def extract(self, filename, path):   
        if not filename.endswith('/'):   
            f = os.path.join(path, filename)   
            dir = os.path.dirname(f)   
            if not os.path.exists(dir):   
                os.makedirs(dir)   
            file(f, 'wb').write(self.zfile.read(filename))   
              
          
def create(zfile, files):   
    z = ZFile(zfile, 'w')   
    z.addfiles(files)   
    z.close()   
      
def extract(zfile, path):   
    z = ZFile(zfile)   
    z.extract_to(path)   
    z.close() 

def zip_Folder(folder,dst):
    startdir = folder  #要压缩的文件夹路径
    #创建存储路径
    parent_path = os.path.dirname(dst)
    if os.path.exists(parent_path):
        pass
    else:
        os.makedirs(parent_path)
    #压缩
    file_news = dst +'.zip' # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) #参数一：文件夹名
    
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()
def main():
    #需要处理的藏经路径
    path = '/media/xian/tripitaka/QS/QS_Compress'
    #处理后压缩包存储路径
    zip_path = '/media/xian/tripitaka/QS/QS_SMALL_ZIP'
    folders = os.listdir(path)
    # folders = ['31']
    for folder in folders:
        oldFolder = os.path.join(path,folder)
        newFolder = os.path.join(zip_path,folder)
        # zip_dir(oldFolder,os.path.dirname(oldFolder))
        zip_Folder(oldFolder,newFolder)
        
        
if __name__ == '__main__':
    main()