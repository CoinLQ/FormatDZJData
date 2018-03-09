#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤：
# 步骤7：检查是否将全部图片进行了压缩。（对应代码：compare_folder.py）
#（注意，这里有需要手动调整的地方：main方法中需要比较的两个folder路径path1和path2）
#*****************************************************************************
import os
import sys
import json
import random
import image 
from PIL import Image
import zipfile
#*********************************founctions*************************************

def compare_folder(folder1,folder2):
    '''
    判断文件夹下所有文件（去除后缀）是否完全一致，一致返回True，否则False
    '''
    if os.path.isfile(folder1) or os.path.isfile(folder2):
        name1 = os.path.basename(folder1)
        name2 = os.path.basename(folder2)
        #去除扩展名
        index1 = name1.rfind('.')  
        if index1 >= 0:
            name1 = name1[:index1]  

        index2 = name2.rfind('.')  
        if index2 >= 0:
            name2 = name2[:index2]  
        #比较文件名
        if name1 == name2:
            return True
        else:
            print('folder1:',folder1,'--','folder2:',folder2)
            # return False
    else:

        files1 = os.listdir(folder1)
        files2 = os.listdir(folder2)
        newfiles1 = []
        newfiles2 = []
        #去除扩展名
        for name in files1:
            index = name.rfind('.')  
            if index >= 0:
                name = name[:index]  
            newfiles1.append(name)  
        for name in files2:
            index = name.rfind('.')  
            if index >= 0:
                name = name[:index]
            newfiles2.append(name) 
        
        if len(list(set(newfiles1).difference(set(newfiles2))))==0 and len(list(set(newfiles2).difference(set(newfiles1))))==0:
            for file in files1:
                filepath1 = os.path.join(folder1,file)
                filepath2 = os.path.join(folder2,file)
                if os.path.isdir(filepath1) and os.path.isdir(filepath2):
                    if compare_folder(filepath1,filepath2):
                        continue
                    else:
                        # print('--filepath1:',filepath1,'--','filepath2:',filepath2)
                        pass
                        # return False
                    
                else:
                    name1 = os.path.basename(filepath1)
                    name2 = os.path.basename(filepath2)
                    #去除扩展名
                    index1 = name1.rfind('.')  
                    if index1 >= 0:
                        name1 = name1[:index1]  

                    index2 = name2.rfind('.')  
                    if index2 >= 0:
                        name2 = name2[:index2]  
                    #比较文件名
                    if name1 == name2:
                        continue
                    else:
                        print('filepath1:',filepath1,name1,'--','filepath2:',filepath2,name2)
                        # return False
            return True
        else:
            # print('folder1:',folder1,'--','folder2:',folder2)
            if len(list(set(newfiles1).difference(set(newfiles2)))) > 0:
                # print ('not in folder2:',list(set(newfiles1).difference(set(newfiles2)))) # b中有而a中没有的
                for shorname in list(set(newfiles1).difference(set(newfiles2))):
                    if 'f' in shorname or 'b' in shorname:
                        pass
                    else:
                        print(shorname)
            # if len(list(set(newfiles2).difference(set(newfiles1)))) > 0:
            #     print ('not in folder1:',list(set(newfiles2).difference(set(newfiles1)))) # a中有而b中没有的
            # return False
         
        
    

def main():
    path1 = '/media/xian/tripitaka/QS/QS_Compress'
    path2 = '/media/xian/tripitaka/QS0/QS_Compress'
    
    print(compare_folder(path1,path2)) 

if __name__ == '__main__':
    main()