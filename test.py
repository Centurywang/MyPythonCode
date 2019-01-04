
def print1(name,**args):
    print(name,args)


def addLabel(**args):
# name = tk.Label(text=text)
# name.grid(column=column, row=row)
    for key,value in zip(args.keys(),args.values()):
        print1(name=1,key=value)
    #print1(name = 1,)
addLabel(name = '1',row=1,colum=3,a = 4,z = 5)