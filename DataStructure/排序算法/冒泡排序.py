
def func(alist):
    length=len(alist)
    for i in range(1,length):
        for j in range(length-i):
            if alist[j]>alist[j+1]:
                temp=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=temp

    return alist


alist=[8,3,4,5,6,7,1,3]

#print(alist[3])
print(func(alist))