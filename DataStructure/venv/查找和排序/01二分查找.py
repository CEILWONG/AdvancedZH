

def binarysearch(alist,item):

        first=0
        last=len(alist)-1

        while first <= last:

            mid = (first + last) // 2
            if alist[mid]==item:
                return mid
            elif alist[mid]<item:
                first=mid+1
                #print(first)
            else:
                last=mid-1
                #print(last)

        return 000

t=binarysearch([0,1,2,3,5,6,7,8,10,27,90,100,102],90)
print(t)