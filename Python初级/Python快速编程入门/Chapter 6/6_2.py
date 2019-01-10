'''
编写函数，求出"1/（1*2）-1/(2*3)+1/(3*4)-1/(4*5)+...."
前n项的和，函数以n（用户输入）为参数
'''

def sum_n1(n):
    num_number = 0
    a = 1
    while n >= a:
        if a % 2 == 0:
            num_number -= 1.0 / (a*(a+1))
        else:
            num_number += 1.0 / (a*(a+1))
        a += 1
    return num_number

def sum_n2(n):
    sum_number = 0
    while n >= 1:
        if n % 2 == 0:
            sum_number -= 1.0 / (n*(n+1))
        else:
            sum_number += 1.0 / (n*(n+1))
        n -= 1
    return sum_number

if __name__ == '__main__':
    n = int(input('请输入n：'))
    result1 = sum_n1(n)
    result2 = sum_n2(n)
    print('结果为：\n {}\t {} '.format(result1,result2))
