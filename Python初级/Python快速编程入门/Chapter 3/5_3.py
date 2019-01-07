'''
编写一个程序，输出9*9乘法表
1 * 1 = 1
1 * 2 = 2   2 * 2 = 4
1 * 3 = 3   2 * 3 = 6

'''

for i in range(1,10):
    for z in range(1,i+1):
        print("{}*{}={}".format(z,i,z*i),end=' ')
        if z == i:
            print('\n')
