

#十进制到二进制的转换的关键在与：十进制连续的除以二，剩下的余数则是零或者是一，把他从后往前串起来就是传说中的二进制所得的数。



class Stack():

    def __init__(self):

        self.item=[]

    def push(self,i):
        self.item.append(i)
        #print("push"+str(i))

    def pop(self):

        Lastnum=self.item[-1]
        self.item=self.item[0:len(self.item)-1]
        return Lastnum

    def isEmpty(self):
        if len(self.item)==0:
            return True
        else:
            return False




def TransTwo(Num):
    s=Stack()

    while Num>0:

        index=Num%2
        s.push(index)

        Num=Num//2

    #print("end")

    str=[]

    while not s.isEmpty():
        str.append(s.pop())

    return str



def main():
    num_10s=int(input("input it:"))

    print(TransTwo(num_10s))

main()