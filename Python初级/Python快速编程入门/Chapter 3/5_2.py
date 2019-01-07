'''
编写一个程序，判断用户输入的数是正数还是负数
'''

number = int(input('Please enter the number:'))

if number > 0:
    print('The number is positive number.')
elif number < 0:
    print('The number is minus.')
else:
    print('The number is 0.')
