

def pushin(alist):

    n=len(alist)

    for i in range(1,n):
        for j in range(i):
            if alist[j]>alist[i]:
                temp=alist[i]
                for k in range(i,j,-1):
                    alist[k]=alist[k-1]
                alist[j]=temp
                #print(i)
                #print(j)
                #print(temp)
                #print(alist)
                break

    return alist

print(pushin([2,6,3,7,4,9,11,0,46,34]))
