

def merge_sort(alist):
    n=len(alist)
    if n=1:
        return alist

    mid=n//2
    left=merge_sort(alist[:mid])
    right=merge_sort(alist[mid:])

    k=[]
    while left and right:
        if left[-1]<right[-1]:
           k.append(left.pop())
        else:
            k.append(right.pop())

    k.extend(right if right else left)

    return k