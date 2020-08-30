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



def HotTomato(m,n):
    q=Queue()
    for i in range(1,m+1):
        q.enqueue(i)
    num=1
    while q.size()!=1:
        temp=q.dequeue()
        if num%n!=0:
            q.enqueue(temp)
        num=num+1
    return q.dequeue()

print(HotTomato(6,3))
