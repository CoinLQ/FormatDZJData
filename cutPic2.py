# -*- coding:utf-8 -*-
from PIL import Image
import os

def cut(id, vx, vy,img_path):
    # # 打开图片图片1.jpg
    name1 = img_path
    # img_path_new = img_path.replace('\\','/')
    # keyList = img_path_new.split("/")
    # length = len(keyList)
    # numberString = keyList[length-2]
    # number = (int)(numberString.split("《乾隆大藏經》")[1])
    
    #文件的前两级目录
    # grader_father=os.path.abspath(os.path.dirname(img_path)+os.path.sep+"..")
    father_path = os.path.dirname(img_path)
    oldFileName = os.path.basename(img_path).split(".jpg")[0]
    newFileName = oldFileName
    name2 = father_path +"/" + newFileName
    #创建存储路径
    parent_path = os.path.dirname(name2)
    if os.path.exists(parent_path):
        pass
    else:
        os.makedirs(parent_path)
    im = Image.open(name1)
    w,h=im.size  
    print (w,h)
    vx = h
    vy = w/2
    # 偏移量
    dx = vx
    dy = vy
    n = 1

    # 左上角切割
    x1 = 0
    y1 = 0
    x2 = vx
    y2 = vy
    print (im.size)  # im.size[0] 宽和高
    w = im.size[0]  # 宽
    h = im.size[1]  # 高

    # 纵向
    while x2 <= h:
        # 横向切
        while y2 <= w:
            if n == 1:
                indexName = "A"
            elif n == 2:
                indexName = "B"
            else:
                indexName = str(n)
            name3 = name2 + indexName + ".jpg"
            # print n,x1,y1,x2,y2
            im2 = im.crop((y1, x1, y2, x2))
            im2.save(name3)
            y1 = y1 + dy
            y2 = y1 + vy
            n = n + 1
        x1 = x1 + dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy

    print ("图片切割成功，切割得到的子图片数为")
    return n - 1
#********************E、遍历文件夹功能************************************
#遍历文件夹，获取所有文件路径
def myEachFiles(path):
    _pathList=[]
    filepath = path
    fileType1 = '.jpg'
    fileType2 = '.xls'
    if os.path.isdir(filepath):
        pathDir =  os.listdir(filepath)
        for allDir in pathDir:
            numberString = allDir
            try:
                number = (int)(numberString.split("《乾隆大藏經》")[1])
                if number < 0:
                    continue
                else:
                    print("pass")
                    pass
            except Exception as e: 
                pass
            
            child = os.path.join('%s/%s' % (filepath, allDir))
            if os.path.isdir(child):
                _pathList.append(myEachFiles(child))
                pass
            else:
                typeList = os.path.splitext(child)
                if typeList[1] == fileType1 :#check file type:.jpg
                    _pathList.append(child)
                    #print('child:','%s' % child.encode('utf-8','ignore'))
                    pass
                else:#not .jpg
                    pass
            
        pass
    else:
        typeList = os.path.splitext(filepath)
        if typeList[1] == fileType1 :#check file type:.jpg
            _pathList.append(filepath)
            pass    
        
        
        #print ('---',child.decode('cp936') )# .decode('gbk')是解决中文显示乱码问题
    return _pathList
#整理文件路径，统一放到一个列表当中，便于使用
def getFilePath(pathList):
    filePathList = []
    fileType1 = '.jpg'
    fileType2 = '.xls'
    for index in pathList:
        if type(index) is list:
            for item in getFilePath(index):
                typeList = os.path.splitext(item)
                if typeList[1] == fileType1 :#check file type:.jpg
                    filePathList.append(item)
                
            
            pass  
        else:
            typeList = os.path.splitext(index)
            if typeList[1] == fileType1 :#check file type:.jpg
                filePathList.append(index)
                pass
    return filePathList
if __name__ == "__main__":
    #获取文件夹路径
    path = input('请输入要切割图片路径：') 
    # path = r"G:\乾隆大藏经压缩后图片"
    # #遍历文件夹
    # pathList = myEachFiles(path)
    # #整理文件路径
    # filePathList = getFilePath(pathList)
    # #循环转换文件内容
    # for x in range(len(filePathList)):
    #     print(len(filePathList),'  ',x)
    #     filePath = filePathList[x]
    #     print(filePath)
    #     # 取图片id的后两位
    #     id = "1"

    #     # 切割图片的面积 vx,vy
    #     # 大
    #     res = cut(id, 1200, 600,filePath)
    res = cut(id, 1200, 600,path)

    
