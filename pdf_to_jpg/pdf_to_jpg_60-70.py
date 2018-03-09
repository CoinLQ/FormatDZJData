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
        # geometry = img.size()
        # w, h = geometry.width(), geometry.height()
        # new_width = 1200
        # factor = new_width/float(w)
        # new_height = int(h * factor)
        # img.resize("{}x{}".format(new_width, new_height))
        #im.read(pdffilename + '[' + str(p) +']')  
        img.write(os.path.join(father_path,str(p+1)+ '.jpg'))  

def main():
    path = '/media/xian/tripitaka/ZC0/ZC'
    files = os.listdir(path)
    for file in files:
        number = int(os.path.basename(file)[-7:-4])
        if number >= 60 and number < 70:
            pdf_path = os.path.join(path,file)
            pdf_to_jpg(pdf_path)
    # pdf_path = input('pdf_path:')
    # pdf_to_jpg(pdf_path)

if __name__ == '__main__':
    main()
