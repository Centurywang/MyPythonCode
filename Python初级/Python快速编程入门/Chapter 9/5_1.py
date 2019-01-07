'''
假设成年人的体重和身高存在此种关系
    身高(厘米) - 100 = 标准体重(千克)
如果一个人的体重与其标准体重的差值在正负 5% 之间，显示“体重正常”，其它则显示“体重超标”或“体重不达标”。
编写程序，能处理用户输入的异常，并且使用自定义异常类来处理身高小于30cm、大于250cm的异常情况
'''



try:
    weight = int(input('请输入体重(千克)：'))
    height = int(input('请输入身高(厘米)：'))
    normalWeight = height - 1000
    difference = float(normalWeight) / abs(normalWeight - weight)
    if difference > 5/100:
        print('体重正常')
    else:
        print('体重不达标')
except:
    print('输入错误')

