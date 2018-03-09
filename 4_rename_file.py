#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 大藏经图片处理步骤： 
# 步骤4：对图片进行重命名，并生成对应卷的命名对照表（用于取消重命名），
# 并生成检查页码图片（存储到dest文件夹，用于抽样检查命名是否正确）.
# （对应代码：renameFile.py，注意，先检查重命名是否完全正确再进行下一步，不然一旦出错后面也需要改正）
#*****************************************************************************
import os
import sys
import json
import random
import image 
from PIL import Image
import numpy as np

FILETYPES = ['.jpg','.tiff','.png']
TP = 'ZC'
TP_DATA = '_Compress'
ZJ_PATH = '/media/xian/tripitaka/'+TP    #藏经根目录
DATA_PATH = ZJ_PATH + '/'+TP+TP_DATA        #藏经目录
DEST_IMG_PATH = ZJ_PATH + '/dest'       #切割图片存储目录
NAMEFILE = ZJ_PATH + '/names/'          #命名信息存储目录（便于取消重命名）
# REGIN_1 = (40, 2300, 300, 2500)       #使用GIMP软件查看图片坐标
# REGIN_2 = (1400, 2200, 1700, 2500) 
REGIN_1 = 1
REGIN_2 = 2
#*********************************founctions*************************************
#founctions1:读取json文件，返回json对象
def readJsonFile(filePath):
    with open(filePath,'r') as f:
        text = f.read()
        text = text.replace('\n','')
        f.close()
    return json.loads(text)
#write file
def writeFile(path,content):
    father_path = os.path.dirname(path)
    if not os.path.exists(father_path):
        os.makedirs(father_path)
    with open(path,'w') as f:
        f.write(content)

#founction2:遍历文件夹，获取所有文件路径
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

#founction3:整理txt文件路径，统一放到一个列表当中，便于使用
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
   

def cancleChangeName(nameDic):
    dict_ori = nameDic
    dict_new = {value:key for key,value in dict_ori.items()}
    return dict_new
def getNameDic(dataDic,path):
    reel_no = dataDic['no']
    total_pages = dataDic['total']
    start_page = dataDic['start']
    end_page = dataDic['end']
    jsonDic = dict()
    names = os.listdir(path)
    for name in names:
        page = int(os.path.splitext(name)[0])
        if page < start_page:
            newPage = 'f' + str(page)
        elif page > end_page:
            newPage = 'b' + str(page-end_page)
        else:
            oldPage = page-start_page+1
            newPage = str(oldPage)
            if reel_no == 3:#json中正文终止页码写错了
                pass
            elif reel_no == 12:#第176，177页缺失
                if oldPage >=176:
                    newPage = str(oldPage+2)
            elif reel_no == 17:#第817，818页缺失
                if oldPage >=817:
                    newPage = str(oldPage+2)
            elif reel_no == 24:#第580，581页多余
                if oldPage >=580:
                    newPage = str(oldPage-2)
            elif reel_no == 26:#第12,13，364,365页缺失，正文574往后缺失
                if oldPage >=12 and oldPage < 364:
                    newPage = str(oldPage+2)
                if oldPage >=364:
                    newPage = str(oldPage+4)
            elif reel_no == 29:#第2，3，62，63页多余
                if oldPage >=2 and oldPage < 62:
                    newPage = str(oldPage-2)#####第34册，PDF顺序有误（第817-824页）
                if oldPage >=62:
                    newPage = str(oldPage-4)
            elif reel_no == 40:#第772-777页多余（实际是：第766-773页多余）----------------------------------------有问题
                if oldPage >=766:
                    newPage = str(oldPage-7)
            elif reel_no == 45:#第860，861页缺失
                if oldPage >=860:
                    newPage = str(oldPage+2)
            elif reel_no == 55:#第842，843页缺失
                if oldPage >=842:
                    newPage = str(oldPage+2)
            elif reel_no == 62:#第430，431页缺失
                if oldPage >=430:
                    newPage = str(oldPage+2)
            elif reel_no == 64:#第页缺失
                if oldPage >=430:
                    newPage = str(oldPage+2)
            elif reel_no == 67:#第744，745页多余
                if oldPage >=744:
                    newPage = str(oldPage-2)
            elif reel_no == 68:#第844，845页缺失
                if oldPage >=844:
                    newPage = str(oldPage+2)
            elif reel_no == 73:#第140-147页多余，
                if oldPage >=140:
                    newPage = str(oldPage-8)
            elif reel_no == 81:#第520,521，616,617页缺失
                if oldPage >=520 and oldPage < 616:
                    newPage = str(oldPage+2)
                if oldPage >= 616:
                    newPage = str(oldPage+4)
            elif reel_no == 95:#第412，413页缺失
                if oldPage >=412:
                    newPage = str(oldPage+2)
            elif reel_no == 97:#json中正文终止页码写错了
                pass
            elif reel_no == 102:#第832，833页缺失
                if oldPage >=832:
                    newPage = str(oldPage+2)
            elif reel_no == 114:#第234，235，873，874页缺失
                if oldPage >=234 and oldPage < 873:
                    newPage = str(oldPage+2)
                if oldPage >= 873:
                    newPage = str(oldPage+4)
            
        jsonDic[str(page)] = TP + '_'+'{:d}'.format(reel_no)+'_'+ newPage
    return jsonDic



#***************************重命名图片校对（通过切图获得页码，比对页码是否与名字相符）************************************
#生成藏经页码字典
def generate_p_dict(tp, img_dir):
    '''
    生成藏经页码字典
    :param tp:
    :return:
    '''
    p_dict = dict()
    for vol in os.listdir(os.path.join(img_dir, tp)):
        p_dict[vol]=len([i for i in os.listdir(os.path.join(img_dir, tp, vol)) ])
    return p_dict
#对随机图片切图
def get_random_page(tp, img_dir,vol,randomNum):
    '''
    :param tp:
    :return:
    '''
    tp_data = tp+TP_DATA
    if vol:
        # rand_no = int(p_dict[vol] * random.random(randomNum))
        
        if randomNum > 2:
            rand_no = int(random.randint(1,randomNum))
        else:
            rand_no = 2
        for filetype in FILETYPES:
            rand_page = os.path.join(img_dir, tp_data, vol, "{}_{}_{:d}".format(tp, vol, rand_no)+filetype)
            if os.path.exists(rand_page):
                picType = filetype
                break
        if not os.path.exists(rand_page):
            print('get_random_page error:path does not exist.',rand_page)
            return
        
        #使用GIMP软件查看图片坐标
        if rand_no % 2 == 0:
            
            region = REGIN_2
        else:
            
            region = REGIN_1
            
        croppageno(rand_page, os.path.join(DEST_IMG_PATH, tp, 'check_big', vol+'_%d%s' % (rand_no, picType)), region)
def get_first_page(tp, img_dir,vol,randomNum):
    '''
    :param tp:
    :return:
    '''
    tp_data = tp+TP_DATA
    if vol:
        # rand_no = int(p_dict[vol] * random.random(randomNum))
        rand_no = randomNum#first page
        for filetype in FILETYPES:
            rand_page = os.path.join(img_dir, tp_data, vol, "{}_{}_{:d}".format(tp, vol, rand_no)+filetype)
            if os.path.exists(rand_page):
                picType = filetype
                break
        if not os.path.exists(rand_page):
            print('get_random_page error:path does not exist.',rand_page)
            return
       
        if rand_no % 2 == 0:
            
            region = REGIN_2
        else:
            
            region = REGIN_1
            
        croppageno(rand_page, os.path.join(DEST_IMG_PATH, tp, 'check_big', vol+ '_%d%s' % (rand_no, picType)), region)

def get_last_page(tp, img_dir,vol,randomNum):
    '''
    :param tp:
    :return:
    '''
    tp_data = tp+TP_DATA
    if vol:
        # rand_no = int(p_dict[vol] * random.random(randomNum))
        rand_no = randomNum #last page
        for filetype in FILETYPES:
            rand_page = os.path.join(img_dir, tp_data, vol, "{}_{}_{:d}".format(tp, vol, rand_no)+filetype)
            if os.path.exists(rand_page):
                picType = filetype
                break
        if not os.path.exists(rand_page):
            print('get_random_page error:path does not exist.',rand_page)
            return
        
        if rand_no % 2 == 0:
           
            region = REGIN_2
        else:
            
            region = REGIN_1
            
        croppageno(rand_page, os.path.join(DEST_IMG_PATH, tp, 'check_big',vol+ '_%d%s' % (rand_no, picType)), region)
#保存切图
def croppageno(img_path, save_path, region):
    try:
        im = Image.open(img_path)
        
        if region == 1:
            x1 = 0
            x2 = x1+800
            y1 = im.size[1]-400
            y2 = im.size[1]
        else:
            x1 = im.size[0]-800
            x2 = im.size[0]
            y1 = im.size[1]-400
            y2 = im.size[1]
        REGIN = (x1,y1,x2,y2)
        imc = im.crop(REGIN)
        father_path = os.path.dirname(save_path)
        if not os.path.exists(father_path):
            os.makedirs(father_path)
        
        imc.save(save_path)
        im.close()
        imc.close()
    except IOError as e:
        print('croppageno error:',e,' -->page:',img_path)
    
#拿到每一卷最后一张图
def get_small_im(tp, page_range, region):
    for page_no in page_range:
        for vol in os.listdir(ZJ_PATH):
            if vol not in ['001', '002']:
                ims = os.listdir(os.path.join(ZJ_PATH, vol))
                ims = sorted(ims, key=lambda X: int(X.split('.')[0]))
                croppageno(os.path.join(ZJ_PATH, vol, ims[page_no - 1]), os.path.join(DEST_IMG_PATH, tp, vol + ' ' + ims[page_no - 1]), region)


#********************************************RENAME---CANCLE---CHECK**************************************************************
#founction4:根据路径对文件重命名
def renameFile(jsonFile,path):
    # read json file
    jsonData = readJsonFile(jsonFile)
    #获得卷序号
    reel_no = os.path.basename(path)
    # get new name dict
    for dataDic in jsonData:
        if int(reel_no) == dataDic['no']:
            nameDic = getNameDic(dataDic,path)
            break
    
    # read files
    pathList = myEachFiles(path)
    files = getFilePath(pathList)
    dic={}
    
    # rename file
    for file in files:
        (filepath,tempfilename) = os.path.split(file);  
        (shortname,extension) = os.path.splitext(tempfilename); 

        # name_split = file.split('/')
        # sutra = name_split[-4]
        # vol = name_split[-2]
        # page = shortname
        # newname = sutra+'_'+str(vol)+'_'+str(page)
        

        try:
            newname = nameDic[shortname]
        except Exception as e:
           print(e,file)
           continue
        
        dst = os.path.join(filepath,newname+extension)
        try:
            os.rename(file, dst)
            dic[file] = dst
        except IOError as e:
            print('rename error:',e)
            pass
    vol = path.split('/')[-1]
    writeFile(os.path.join(NAMEFILE,vol+'.json'),json.dumps(dic))
#校对重命名是否成功
def checkRenameFile(jsonFile,path):
    # read json file
    jsonData = readJsonFile(jsonFile)
    #获得卷序号
    reel_no = os.path.basename(path)
    
    # get new name dict
    nameDic = cancleChangeName(jsonData)
    
    # read files
    pathList = myEachFiles(path)
    files = getFilePath(pathList)
    # rename file
    changes = list()
    for file in files:
        (filepath,tempfilename) = os.path.split(file);  
        (shortname,extension) = os.path.splitext(tempfilename); 
        if 'f' in shortname or 'b' in shortname:
            continue
        newname = nameDic[file]
        changes.append(newname)
    
    for i in range(5):
        try:
            randomNum = len(changes)
            tp = TP
            if i == 0:
                get_first_page(tp,ZJ_PATH,reel_no,1)
            elif i==1:
                get_last_page(tp,ZJ_PATH,reel_no,randomNum)
            else:
                get_random_page(tp,ZJ_PATH,reel_no,randomNum-1)
            
        except IOError as e:
            print('cut page pic error:',e)
            pass

def cancleRenameFile(jsonFile,path):
    # read json file
    jsonData = readJsonFile(jsonFile)
    #获得卷序号
    reel_no = os.path.basename(path)
    # get new name dict
    nameDic = jsonData
    # cancle change name
    nameDic = cancleChangeName(nameDic)
    # read files
    pathList = myEachFiles(path)
    files = getFilePath(pathList)
    
    # rename file
    for file in files:
        (filepath,tempfilename) = os.path.split(file);  
        (shortname,extension) = os.path.splitext(tempfilename);  
        newname = nameDic[u'%s'%file]
        # dst = os.path.join(filepath,newname+extension)
        try:
            os.rename(file, newname)
        except IOError as e:
            print('rename error:',e)
            pass
    
#************************************MAIN*************************************************************************
def main():
    
    choice = '3'
    length = len(os.listdir(DATA_PATH))
    # vols = [3,12,17,24,26,29,40,45,55,62,64,67,68,73,81,95,97,102,114]
    # vols = [26,64,114]
    vols = [3,12,17,24,26,29]
    
    for x in vols:
        path = DATA_PATH + '/{:d}'.format(x)
        if choice == '1':
            #rename files
            # read json file and find pic file
            jsonFile = '/media/xian/tripitaka/ZC/zc_vol_page.json' 
            renameFile(jsonFile,path)
        elif choice == '2':
            #check files
            jsonFile = os.path.join(NAMEFILE,str(x)+'.json')
            checkRenameFile(jsonFile,path)
            pass
        elif choice == '3':
            #cancle rename files
            jsonFile = os.path.join(NAMEFILE,str(x)+'.json')
            cancleRenameFile(jsonFile,path)
            pass
        else:
            print('sorry,not get it.')
    print('The end.')
        
    
    
    
    
    
if __name__ == '__main__':
    main()