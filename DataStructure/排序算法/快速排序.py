#思考有问题，可以自己在想一想
def func(alist):
    length=len(alist)
    if length==1:
        return alist

    mid_num=alist[0]
    left=1
    right=length-1
    while left<right:
        while alist[left]<mid_num:
            left=left+1
        while alist[right]>mid_num:
            right=right-1

        temp=alist[left]
        alist[left]=alist[right]
        alist[right]=temp

    else:
        if alist[right]<mid_num:
            temp=alist[right]
            alist[right]=alist[0]
            alist[0]=temp

    func(alist[:right])
    func(alist[right:])
    return alist

alist=[8,4,5,6,2,4,6,4,6,9,45,76]
print(func(alist))