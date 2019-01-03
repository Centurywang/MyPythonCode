'''
实现两个数的交换
'''

# 第一种 设第三个数作为中间变量
a = 1
b = 2
print('交换前 a=%d b=%d'%(a,b))
c = a
a = b
b = c
print('交换后 a=%d b=%d'%(a,b))

# 第二种 python特有
a = 1
b = 2
print('交换前 a=%d b=%d'%(a,b))
a,b = b,a
print('交换后 a=%d b=%d'%(a,b))