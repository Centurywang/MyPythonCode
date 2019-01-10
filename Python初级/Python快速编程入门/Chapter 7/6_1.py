'''
已知一个列表 [1,2,3,4,5]，让列表每个元素+1，把结果不能被二整除的元素筛选出来。
'''

list1 = [1,2,3,4,5]
# 列表元素+1
list2 = list(map(lambda x: x+1,list1))
# 把结果不能被二整除的元素筛选出来
list3 = list(filter(lambda x:x%2!=0,list2))
print('列表元素+1：{}\n结果不能被二整除：{}'.format(list2,list3))
