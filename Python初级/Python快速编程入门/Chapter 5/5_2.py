'''
用户输入一个字符串，将下标为偶数的字符提出来合并成一个新的字符串A，再将下标为奇数的字符提出来合并成一个新的字符串B，再将AB连接起来并输出
'''


def func(strs):
    A = ''
    B = ''
    for x,y in enumerate(strs):
        if x % 2 == 0:
            A += y
        else:
            B += y
    return A+B

if __name__ == '__main__':
    strs = input('请输入：')
    print(func(strs))