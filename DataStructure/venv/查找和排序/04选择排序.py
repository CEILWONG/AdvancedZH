def select(alist):

    n=len(alist)
    #maxpos=0
    for i in range(n-1,0,-1):
        maxpos=0
        for j in range(i+1):
            if alist[j]>=alist[maxpos]:
                maxpos=j
        temp=alist[maxpos]
        alist[maxpos]=alist[i]
        alist[i]=temp
        #break

    return alist

print(select([2,4,1,67,34,56,24,78]))