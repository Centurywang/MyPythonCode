'''
用户输入一个字符串，请将字符串中的所有字母全部向后移一位，最后一个字母放到字符串的开头，最后将新的字符串输出
'''

def func1(strs):
    strs = strs[-1]+strs[:-1]
    return strs
if __name__ == '__main__':
    strs = input('请输入：')
    print(func1(strs))