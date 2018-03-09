#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤：
# 步骤6：获取每一卷图片高度信息，以{图片名：图片高度}为键值对，写入json文件中（后台需要）。（对应代码：get_pic_json.py）
#（注意，这里有两个地方需要手动调整（main方法中）：1、要处理的藏经文件夹路径；2、处理后的json数据存储路径。）
#*****************************************************************************
import os
import sys
import json
import random
import image 
from PIL import Image
import shutil
import codecs

FILETYPES = ['.jpg','.tiff','.png']
zj_path = '/media/xian/tripitaka/'
dest_img_path = '/media/xian/tripitaka/dest'
#*********************************founctions*************************************
#******************B、写文件功能******************************
def writeFile(filePath,content):
    parent_path = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    if os.path.exists(parent_path):
        pass
    else:
        os.makedirs(parent_path)
    
    try:
        newPath = os.path.join(parent_path,fileName)
        # fopen = codecs.open(newPath,'r')
        # fopen.close()

        fopen = codecs.open(newPath, 'w','utf-8')
        fopen.write('%s%s' % (content, os.linesep))
        fopen.close()
        return True
    except Exception as e:
        print('write file exception:',e)
        return False 
    else:
        return False
def get_pic_height(path):
    try:
        img = Image.open(path)
        height = img.size[1]
    except :
        height = ''
        print('get_pic_height error:',path)
      
    return height
    pass
def get_pic_name(path):
    name = os.path.splitext(os.path.basename(path))[0]
    return name

def main():
    dic = dict()
    #要处理的藏经文件夹路径，手动调整
    data_path = '/media/xian/tripitaka/QS/QS_Compress'
    #生成json数据存储路径，手动调整
    json_path = '/media/xian/tripitaka/QS/QS_JSON'
    for x in range(1,121):
        path = data_path + '/%d' % x
        if not os.path.isdir(path):
            continue
        files = os.listdir(path)
        for file in files:
            height = get_pic_height(os.path.join(path,file))
            name = get_pic_name(os.path.join(path,file))
            # if height == 1678:
            #     continue
            dic[name] = height
        #write json file
        jsonData = json.dumps(dic)
        outfile = os.path.join(json_path,str(x)+'.json')
        writeFile(outfile,jsonData)
        dic.clear()
        jsonData = None
        print(outfile)
    # #write json file
    # jsonData = json.dumps(dic)
    # outfile = os.path.join('/media/xian/tripitaka/QS/QS_JSON','QS.json')
    # writeFile(outfile,jsonData)
    # dic.clear()
    # jsonData = None
    # print(outfile)
    

if __name__ == '__main__':
    main()