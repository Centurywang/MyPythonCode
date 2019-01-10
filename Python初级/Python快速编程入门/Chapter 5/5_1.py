'''
编写一个函数，用于判断用户输入的字符串是否由小写字母和数字组成
'''

def func1(strs):
    for s in strs:
        if 'a'<= s <='z' or '0'<= s <='9':
            pass
        else:
            return False
    return True
# Python isalnum() 方法检测字符串是否由字母和数字组成。
'''该题不正确'''
def func2(strs):
    return strs.isalnum()

if __name__ == '__main__':
    strs = input('请输入字符串：')
    print(func1(strs))

    print(func2(strs))
