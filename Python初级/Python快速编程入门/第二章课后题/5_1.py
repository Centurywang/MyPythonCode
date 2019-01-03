'''
输入直角三角形的两个直角边的长度a、b，求斜边c的长度
'''

# 第一种 c = 根号下 a方 +  b方
a = float(input('请输入边a长度：'))
b = float(input('请输入边b长度：'))
# 第三边长的平方等于两边平方和
c = (a*a + b*b) ** 0.5
print('斜边c的长度为：{}'.format(c))

# 第二种 c方 = a方 + b方
c = a*a + b*b
c = c ** 0.5
print('%.2f'%c)