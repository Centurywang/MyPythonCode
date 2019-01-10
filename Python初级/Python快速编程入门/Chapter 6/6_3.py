'''
回文数是一个正向和逆向都相同的整数，如123454321、9889，编写函数判断一个整数是否是回文数
'''
def judgeHWS1(number):
    number = str(number)
    len_number = len(number)
    for i in range(int(len_number / 2)):
        if number[i] != number[-(i + 1)]:
            return False
    return True

def judgeHWS2(number):
    number = str(number)
    number2 = number[::-1]
    return number == number2

if __name__ == '__main__':
    number = int(input('请输入：'))
    result1 = judgeHWS1(number)
    if result1:
        print('方法一 该数是回文数')
    else:
        print('方法一 该数不是回文数')

    result2 = judgeHWS2(number)
    if result2:
        print('方法二 该数是回文数')
    else:
        print('方法二 该数不是回文数')
