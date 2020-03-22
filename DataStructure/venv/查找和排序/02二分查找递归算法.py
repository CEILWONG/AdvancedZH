

def binarysearch(alist,item):

    first =0
    last =len(alist)-1

    mid=(first+last)//2
    while last>=0:

        if alist[mid]==item:
            return true
        elif alist[mid]<item:
            return binarysearch(alist[first:mid],item)

        else:
            return binarysearch(alist[mid+1:last+1],item)

        return false


print(binarysearch([0,1,2,3,4,5,6,7,8,9],2))


