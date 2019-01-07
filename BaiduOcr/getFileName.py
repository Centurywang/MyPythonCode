'''遍历目录文件名'''
import os

class GetFile():

    def __init__(self,filePath):
        self.filePath = filePath

    def getFilename(self):
        fileList = []
        for filename in os.listdir(self.filePath):
            fileList.append(filename)
        return fileList

from BaiduOcr import BaiduOcr
ocr = BaiduOcr()

# 单个文件 结果直接在GUI显示
def getPictureWords(filePath):
    resu = ocr.print_Text(filePath)
    return resu
# 目录下所有 结果选择要保存的目录对每个图片文字进行保存
def getPicturesWords(directoryPath):
    outPutPath = 'C:\\Users\Century\Desktop\\'
    getFile = GetFile(directoryPath)
    result = getFile.getFilename()
    for i in result:
        print(directoryPath)
        resu = ocr.print_Text(directoryPath + i)
        print(resu)
        with open(outPutPath+i[:-4]+'.txt','w') as f:
            f.write(resu)








'''
import os
for filename in os.listdir(r'images/'):
    print(filename)

import glob
for filename in glob.glob(r'images\*.png'):
    print(filename)
'''