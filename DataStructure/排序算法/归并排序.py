
def merge_sort(alist):
    if len(alist)<=1:
        return alist

    middle=len(alist)//2

    left=merge_sort(alist[:middle])
    right=merge_sort(alist[middle:])

    merged=[]
    while left and right:
        if left[0]<right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)

    return merged


alist=[8,4,5,6,2,4,6,4,6,9,45,76]

print(merge_sort(alist))