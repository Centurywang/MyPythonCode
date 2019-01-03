'''
接受输入的一行字符，统计出字符串中包含数字的个数
'''

# 第一种
strs = input('Please enter a line characters:')
counts = 0
for i in strs:
    try:
        i = int(i)
    except:
        pass
    if i in range(10):
        counts += 1
print('The count is:%d'%counts)
