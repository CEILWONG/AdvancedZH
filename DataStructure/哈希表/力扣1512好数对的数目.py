

def func(alist):
    tmp=[]
    num=[]
    for i in alist:
        if i not in tmp:
            tmp.append(i)
            num.append(1)
        else:
            num[tmp.index(i)]+=1
    allnum=0
    for n in num:
            allnum+=n*(n-1)//2

    return allnum

alist=[1,2,3]

print(func(alist))