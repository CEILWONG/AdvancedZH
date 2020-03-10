mylist=[1,2,3,4,5,6,7,8,9,10]

def addall(list):

    if len(list)==1:
        return list[0]
    else:
        return list[-1]+addall(list[0:len(list)-1])


print(addall(mylist))