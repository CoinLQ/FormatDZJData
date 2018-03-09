#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤：
# 步骤5：对重命名后的图片进行压缩，转化为宽为1200,高度等比例,文件类型为.jpg的新图片，存储到Compress文件夹。（对应代码：compressPic.py）
#（注意，这里有两个地方需要手动调整（main方法中）：1、要处理的藏经文件夹路径；2、处理后的藏经存储路径。）
#*****************************************************************************
from PIL import Image  
import os
FILETYPES = ['.jpg','.tiff']
#图片压缩批处理  
def compressImage(srcPath,dstPath):  
    for filename in os.listdir(srcPath):  
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)        

        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        (shortname,extension) = os.path.splitext(filename);  
        dstFile=os.path.join(dstPath,shortname+'.jpg')

        #如果是文件就处理
        if os.path.isfile(srcFile):     
            #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg=Image.open(srcFile)  
            w,h=sImg.size  
            newW = 1200
            newH = int(1200*h/w)
            dImg=sImg.resize((newW,newH),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            #程序检查通道数，来决定是直接转换成jpg还是丢弃A通道后转换成jpg
            if len(dImg.split()) == 4:
                #prevent IOError: cannot write mode RGBA as JPEG
                r, g, b, a = dImg.split()
                dImg = Image.merge("RGB", (r, g, b))
                dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            else:
                dImg.save(dstFile)
            # print (dstFile+" compressed succeeded")

        #如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile,dstFile)

def compressImageFile(srcFile,dstFile):
    #如果是文件就处理
    if os.path.isfile(srcFile):     
        #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
        sImg=Image.open(srcFile)  
        w,h=sImg.size  
        newW = 1200
        newH = int(1200*h/w)
        dImg=sImg.resize((newW,newH),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
        #程序检查通道数，来决定是直接转换成jpg还是丢弃A通道后转换成jpg
        if len(dImg.split()) == 4:
            #prevent IOError: cannot write mode RGBA as JPEG
            r, g, b, a = dImg.split()
            dImg = Image.merge("RGB", (r, g, b))
            dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
        else:
            dImg.save(dstFile)
    pass

def main():
    # #藏经文件夹路径，手动调整
    # path = '/media/xian/tripitaka/ZC/ZC_DATA'
    # #压缩后文件存储路径，可以手动调整
    # compress_path = '/media/xian/tripitaka/ZC/ZC_Compress'
    # #get files
    # # files = os.listdir(path)
    # files = ['55','56','57','58','59','60','61','62','63']
    # # rename file
    # (filepath,tempfilename) = os.path.split(path);  
    # (shortname,extension) = os.path.splitext(tempfilename); 
   
    # for file in files:
    #     (filepath,tempfilename) = os.path.split(file);  
    #     (shortname,extension) = os.path.splitext(tempfilename); 
    #     dst = os.path.join(compress_path,tempfilename)
        
    #     #create father path
    #     father_path = os.path.dirname(dst)
    #     if not os.path.exists(father_path):
    #         os.makedirs(father_path)
    #     #compress
    #     try:
    #         src = os.path.join(path,file)
    #         compressImage(src,dst)
    #     except IOError as e:
    #         print('compress error:',e,file)
    #         pass
    
    
    # src = input('src_path:')
    src = '/media/xian/tripitaka/ZC/ZC_DATA/5/845.jpg'
    (filepath,tempfilename) = os.path.split(src);  
    (shortname,extension) = os.path.splitext(tempfilename); 
    #压缩后文件存储路径，可以手动调整
    dst = os.path.join('/media/xian/tripitaka/ZC/ZC_Compress','5/845.jpg')
    compressImageFile(src,dst)

if __name__ == '__main__':
    main()


    