#双端队列（环状链表，循环数组）

class Deque(object):

    def __init__(self):
        self.items=[]

    def addFront(self,item):

        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def rmFront(self):
        return self.items.pop()

    def rmRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    d=Deque()

    d.addFront(3)
    d.addFront(4)
    d.addRear("a")
    print(d.size())
    print(d.isEmpty())
    print(d.items)
    d.rmFront()
    print(d.items)

    d.rmRear()
    print(d.items)


main()



