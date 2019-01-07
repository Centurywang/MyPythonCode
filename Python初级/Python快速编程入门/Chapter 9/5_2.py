'''
录入一个学生的成绩，把该学生的成绩转换为A优秀、B良好、C合格、D不及格的形式
最后将该学生的成绩打印出来。要求使用assert断言处理分数不合理的情况
'''

while True:
    try:
        score = float(input('请输入学生成绩：'))
        if score <0 or score>100:
            assert "分数不合理"
        else:
            if score >= 90:
                print('A')
            elif score >= 80:
                print('B')
            elif score >= 60:
                print('C')
            else:
                print('D')
    except Exception as e:
        print(e)
    choice = input('是否继续？(y/n)')
    if choice == 'y' or choice == 'Y':
        pass
    elif choice == 'n' or choice == 'N':
        break
    else:
        print('输入错误！')
        break




