'''
编写函数，求两个正整数的最小公倍数
'''

def judgeLCMM(a,b):
    min = max(a,b)
    LCM = 1
    for i in range(1,min):
       if a%i == 0 and b%i == 0:
           return LCM


if __name__ == '__main__':
    a = int(input('请输入a：'))
    b = int(input('请输入b：'))
    print(judgeLCMM(a,b))