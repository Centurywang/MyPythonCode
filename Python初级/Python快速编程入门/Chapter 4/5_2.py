'''
输入星期几的第一个字母，来判断是星期几，如果第一个字母一样，则继续判断第二个字母，以此类推
星期一 Monday  星期二 Tuesday  星期三 Wednesday  星期四 Thursday
星期五 Friday  星期六 Saturday  星期天 Sunday
'''

weeks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

firN = input('请输入第一个字母：')
count = 0
judgeWeeks = []
for i in weeks:
    if firN == i[0]:
        count += 1
        judgeWeeks.append(i)
if len(judgeWeeks) > 1:
    secN = input('请输入第二个字母：')
    for i in judgeWeeks:
        if secN == i[1]:
            print('该天为%s'%i)
else:
    print('该天为%s'%judgeWeeks[0])





