class Mylist:
    def __init__(self,num):
        self.data=num

    def __iter__(self):
        return MyIterator(self.data)

class MyIterator:
    def __init__(self,data):
        self.start=0
        self.end=data

    def __iter__(self):
        return self

    def __next__(self):

        while self.start<self.end:
            self.start+=1
            return self.start-1
        raise StopIteration


def func1():
    testlist=[0,1,2,3,4]
    it=iter(testlist)
    print(next(it))
    print(next(it))

alist=Mylist(5)
for i in alist:
    print(i)