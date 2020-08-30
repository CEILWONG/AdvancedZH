class Stack:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return self.item==[]

    def push(self,i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item)-1]

    def size(self):
        return len(self.item)


def main():
    s=Stack()
    for i in range(0,5):
        s.push(i)

    while(not s.isEmpty()):
        print(s.pop())

main()