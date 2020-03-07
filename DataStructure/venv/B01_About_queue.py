

class Queue(object):
    def __init__(self):
        self.items=[]


    def En_queue(self,item):
        self.items.insert(0,item)

    def De_queue(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

def main():
    q=Queue()

    q.En_queue("a")
    q.En_queue("b")

    print(q.size())

    print(q.isEmpty())

    print(q.items)

    print(q.De_queue())
    print(q.items)

main()


