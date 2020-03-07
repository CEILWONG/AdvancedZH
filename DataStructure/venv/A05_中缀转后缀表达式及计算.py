#该问题：需要先将中缀表达式转换成后缀表达式，转换完成之后，需要有个函数对后缀表达式进行计算

#第二个就是需要了解后缀表达式的规则，以及转换的算法

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

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        if len(self.item)==0:
            return True
        else:
            return False




def TransLast(MiddleStr):

    priop={}
    priop["+"]=1
    priop["-"]=1
    priop["*"]=2
    priop["/"]=2
    priop["("]=0

    s=Stack()
    list=[]
    for char in MiddleStr:
        if char == "（":
            s.push(char)
        elif char == "+" or char =="-" or char =="*" or char =="/":
            while not s.isEmpty() and (priop[s.peek()]>priop[char] or priop[s.peek()]>priop[char]):
                list.append(s.pop())

            s.push(char)
        elif char==")":

            while not s.peek()=="(":
                list.append(s.pop())
            s.pop()
        else:
            list.append(char)

    while not s.isEmpty():
        list.append(s.pop())

    return " ".join(list)

def ComputeLast(LastStr):
    pass




def main():
    MiddleStr=input("input it:")

    LastStr=TransLast(MiddleStr)

    print(LastStr)

    #print(ComputeLast(LastStr))

main()
