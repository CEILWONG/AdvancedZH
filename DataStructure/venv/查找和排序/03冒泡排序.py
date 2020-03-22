

def pao(alist):

    n=len(alist)

    for i in range(n-1,0,-1):
        for j in range(i):
            if alist[j+1]<alist[j]:
                temp=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=temp
    return alist

print(pao([2,31,5,3,8,55,90,23,7]))

