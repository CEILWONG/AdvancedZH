

#A + B * (C + D) + E

#ABCD+*E+

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


def Middle2After(expressionStr):
    s=Stack()
    strList = expressionStr.split(' ')
    outList=[]
    markvalue={'+':1,'-':1,'*':2,'/':2,'(':0}
    for i in strList:

        if i == '(':
            s.push(i)
        elif i ==')':
            temp=s.pop()
            while temp!='(':
                outList.append(temp)
                temp=s.pop()
        elif i in markvalue:
            while s.size()!=0 and markvalue[s.peek()]>markvalue[i]:
                outList.append(s.pop())
            else:
                s.push(i)
        else:
            outList.append(i)

    while s.size()!=0:
        outList.append(s.pop())

    return outList


def main():
    str='1 + ( 2 + 3 * 5 )'
    print(Middle2After(str))

main()


