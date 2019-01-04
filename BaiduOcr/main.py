import BaiduOcr
import getFileName
import OcrGUI

'''创建窗口'''
# 标题
window = OcrGUI.Window('图片转文字')
# 标签
window.addLabel(name='label1',text='单个图片转文字',column=2,row=0)
window.addLabel(name='label2',text='目录下图片转文字',column=2,row=4)
window.addLabel(name='label3',text='请输入文件路径',column=0,row=2)
window.addLabel(name='label4',text='请输入目录路径',column=0,row=5)
# 输入框
entry1 = window.addEntry(name='entry1',column=2,row=2)
entry2 = window.addEntry(name='entry2',column=2,row=5)


# 单个图片转文字 进行搜索 获取文字Entry,传出文字于TextField
def translation1():
    # 获取输入信息
    filePath = str(entry1.get())
    result = getFileName.getPictureWords(filePath)
    # 显示结果TextField
    window.addTextField('field1',  row=4, text=result)
# , height=300, width=400
def translation2():
    # 获取输入信息
    directoryPath = str(entry2.get())
    # 将结果在桌面写出
    getFileName.getPicturesWords(directoryPath)


#
# 按钮
window.addButton("button1",'确定',4,2,translation1)
window.addButton("button2",'确定',4,5,translation2)

window.run()