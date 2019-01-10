'''
编写一个程序，用于统计字符串中每个字母出现次数（字母忽略大小写）
统计出结果，按照['a':3,'b':4]的格式输出
'''

def count_letter(strs):
    litter = {}
    for i in strs:
        if i in litter.keys():
            litter[i] += 1
        else:
            litter[i] = 1
    return litter

if __name__ == '__main__':
    strs = input('请输入：')
    print(count_letter(strs))


