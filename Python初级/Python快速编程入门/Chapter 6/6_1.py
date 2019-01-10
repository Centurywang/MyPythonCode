'''
定义一个getMax函数，返回键盘输入三个数中的最大值
'''

def getMax_1(number_List):
    return max(number_List)

def getMax_2(number_List):
    max_Number = number_List[0]
    for number in number_List:
        if number > max_Number:
            max_Number = number
    return max_Number

if __name__ == '__main__':
    number_List = []
    for i in range(3):
        number = float(input('请输入数字：'))
        number_List.append(number)
    max_Number1 = getMax_1(number_List)
    max_Number2 = getMax_2(number_List)
    print('输入的最大值为{}\t{}'.format(max_Number1,max_Number2))


