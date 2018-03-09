#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*********************************founction documents**********************************
# 比较文件夹内文件总数和json中记录total值是否一致
#*****************************************************************************
import os,sys
import json

#founctions1:读取json文件，返回json对象
def readJsonFile(filePath):
    with open(filePath,'r') as f:
        text = f.read()
        text = text.replace('\n','')
        f.close()
    return json.loads(text)

def main():
    # read json file
    jsonFile = '/media/xian/tripitaka/ZC/zc_vol_page.json'
    jsonData = readJsonFile(jsonFile)
    father_path = '/media/xian/tripitaka/ZC/ZC_Compress'
    vols = os.listdir(father_path)
    for dataDic in jsonData:
        vol = dataDic['no']
        total_page_json = dataDic['total']
        if str(vol) in vols:
            total_page_data = len(os.listdir(os.path.join(father_path,str(vol))))
            if int(total_page_json) != int(total_page_data):
                print('vol:',vol,'--total_page_json:',total_page_json,'--total_page_data:',total_page_data)
    
    print('Done.')
if __name__ == '__main__':
    main()