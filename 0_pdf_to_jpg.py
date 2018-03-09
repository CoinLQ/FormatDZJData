#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys  
import PyPDF2  
import PythonMagick   
  

def pdf_to_jpg(pdffilename):
     
    pdf_im = PyPDF2.PdfFileReader(file(pdffilename, "rb"))  
    npage = pdf_im.getNumPages()   
    root_path = '/media/xian/tripitaka/ZC'
    vol = os.path.basename(pdffilename)[-7:-4]
    father_path = os.path.join(root_path,vol)
    if not os.path.isdir(father_path):
        os.makedirs(father_path)
    for p in range(npage):  
        img = PythonMagick.Image(pdffilename + '[' + str(p) +']')  
        img.density('300')  
        img.write(os.path.join(father_path,str(p+1)+ '.jpg'))  

def main():
    path = '/media/xian/tripitaka/ZC0/ZC'
    files = [12,17,24,26,29,45,55,62,64,67,68,73,81,95,97,102,114]
    for file in files:
        pdf_path = os.path.join(path,'《趙城金藏》{:03d}'.format(file)+'.pdf')
        pdf_to_jpg(pdf_path)
    # pdf_path = input('pdf_path:')
    # pdf_to_jpg(pdf_path)

if __name__ == '__main__':
    main()
