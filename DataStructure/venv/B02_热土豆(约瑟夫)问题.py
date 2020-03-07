
class Queue(object):

    def __init__(self):
        self.items=[]

    def add(self,item):
        self.items.insert(0,item)

    def dele(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def ComputeYasef(num_people,num_yasef):

    #这里people和数的整数以及大小关系的判断就不写了

    Q=Queue()

    for i in range(1,num_people+1):
        Q.add(i)

    while not Q.size()==1:
        #Q.add(Q.dele())
        for i in range(1,num_yasef):
            tmp=Q.dele()
            Q.add(tmp)
        Q.dele()

    return Q.items



def main():

    num_people=int(input("how many peopele:"))

    num_yasef=int(input("input your yasef num:"))

    print(ComputeYasef(num_people,num_yasef))
    #print()


main()