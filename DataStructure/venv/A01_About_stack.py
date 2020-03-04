

class Stack(object):


    def __init__(self):
        self.items=[]

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self,node):

        self.items.append(node)

    def pop(self):
        return self.items.pop()


    def peek(self):

        return self.items[-1]

    def size(self):
        return len(self.items)


def main():
        wth=Stack()
        t=wth.isEmpty()
        print("isEmpty=%d"%t)
        #print()

        wth.push(1)
        wth.push(2)
        wth.push(3)

        #wth.peek()

        print(wth.pop())
        print(wth.peek())

        print(wth.size())

        print(wth.pop())

        print(wth.size())



main()

