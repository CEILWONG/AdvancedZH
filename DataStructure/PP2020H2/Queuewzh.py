
class Queue:

    def __init__(self):
        self.item=[]

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item==[]

    def enqueue(self,x):
        self.item.insert(0,x)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)


def main():
    q=Queue()
    for i in range(5):
        q.enqueue(i)
    out=[]

    out.append(q.dequeue())
    out.append(q.dequeue())
    print(out)

main()