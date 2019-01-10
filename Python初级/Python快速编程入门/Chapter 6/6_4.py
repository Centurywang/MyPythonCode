'''
编写函数，判断输入的三个数字是否能构成三角形的三条边
'''

def judge_triangle(number1,number2,number3):
    if number1+number2 > number3 and number2+number3 > number1 and number1+number3 > number2:
        return True
    else:
        return False

if __name__ == '__main__':
    number1 = int(input('请输入边长：'))
    number2 = int(input('请输入边长：'))
    number3 = int(input('请输入边长：'))

    if judge_triangle(number1,number2,number3):
        print('输入的三个数能构成三角形的三条边')
    else:
        print('输入的三个数不能构成三角形的三条边')
