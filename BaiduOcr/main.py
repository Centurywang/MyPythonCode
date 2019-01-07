import BaiduOcr
import getFileName
import OcrGUI

import tkinter as tk
'''创建窗口'''
# 标题
window = tk.Tk()
window.title('图片转文字')
window.geometry()
# 标签
label1 = tk.Label(text='单个图片转文字')
label1.grid(column=2, row=0)

label2 = tk.Label(text='目录下图片转文字')
label2.grid(column=2,row=4)

label3 = tk.Label(text='请输入文件路径')
label3.grid(column=0,row=2)

label4 = tk.Label(text='请输入目录路径')
label4.grid(column=0,row=5)
# 输入框
entry1 = tk.Entry()
entry1.grid(column=2,row=2)

entry2 = tk.Entry()
entry2.grid(column=2,row=5)

# 单个图片转文字 进行搜索 获取文字Entry,传出文字于TextField
def translation1():
    # 获取输入信息
    filePath = str(entry1.get())
    print(filePath)
    result = getFileName.getPictureWords(filePath)
    print(result)
    # 显示结果TextField
    textField = tk.Text(master=window, height=10, width=30)
    textField.grid(row=6,column=0)
    textField.insert(tk.END,result)
# , height=300, width=400
def translation2():
    # 获取输入信息
    directoryPath = str(entry2.get())
    # 将结果在桌面写出
    getFileName.getPicturesWords(directoryPath)

# 按钮
button1 = tk.Button(text='确定',command=translation1)
button2 = tk.Button(text='确定',command=translation2)
button1.grid(column=4, row=2)
button2.grid(column=4, row=5)

window.mainloop()