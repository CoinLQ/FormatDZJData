import os
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_KEY='jobs'

def add_upload_job(path):
    r.rpush(REDIS_KEY, path)

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
                number = (int)(numberString)
                if number >= 28 and number < 201 and number != 27:
                    pass
                else:
                    continue
                
                    
            except Exception as e: 
                pass
            
            child = os.path.join('%s/%s' % (filepath, allDir))
            if os.path.isdir(child):
                _pathList.append(myEachFiles(child))
                pass
            else:
                typeList = os.path.splitext(child)
                if 'cutPic' in child:
                    continue
                else:
                    pass
                if typeList[1] == fileType1 or typeList[1] == fileType2:#check file type:.jpg
                    _pathList.append(child)
                    #print('child:','%s' % child.encode('utf-8','ignore'))
                    pass
                else:#not .jpg
                    pass
            
        pass
    else:
        typeList = os.path.splitext(filepath)
        if typeList[1] == fileType1 or typeList[1] == fileType2:#check file type:.jpg
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
                if typeList[1] == fileType1 or typeList[1] == fileType2:#check file type:.jpg
                    filePathList.append(item)
                
            
            pass  
        else:
            typeList = os.path.splitext(index)
            if typeList[1] == fileType1 or typeList[1] == fileType2:#check file type:.jpg
                filePathList.append(index)
                pass
    return filePathList


if __name__=='__main__': 
    #获取文件夹路径
    # path = input('请输入要遍历文件夹路径（一层文件夹）：') 
    path = r"/media/xian/tripitaka/YB_JPG"
    #遍历文件夹
    pathList = myEachFiles(path)
    #整理文件路径
    filePathList = getFilePath(pathList)
    #循环转换文件内容
    for x in range(len(filePathList)):
        filePath = filePathList[x]
        #上传文件
        add_upload_job(filePath)