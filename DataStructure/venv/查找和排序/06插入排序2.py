

def pushin(alist):
    n=len(alist)

    for i in range(1,n):

        value=alist[i]
        pos=i
        while pos>0 and alist[pos-1]>alist[pos]:
            tmp= alist[pos]
            alist[pos]=alist[pos-1]
            alist[pos-1]=tmp

            pos=pos-1
    return alist


print(pushin([6,2,8,4,9,14,2,76,34]))