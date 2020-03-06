class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,x):
        self.item.append(x)

    def pop(self):
        self.item=self.item[0:len(self.item)-1]

    def peek(self):
        return self.item[-1]

    def length(self):
        return len(self.item)






def index(alist,sth):
    index=0
    if sth in alist:
        for x in alist:
            index +=1
            if x==sth:
                return index
    else:
        return -1




def is_balance(Astring):

    s=Stack()
    left=['(','[','{']
    right=[')',']','}']

    for x in Astring:

        if x in left:
            s.push(x)

        elif x in right:
            if s.length()==0:
                return "not balance"
            elif index(right,x)==index(left,s.peek()):
                s.pop()
            else:
                return "not balance"
        else:
            return "there's other word"


    if s.length()==0:
        return "yes,balance"
    else:
        return "not balance"

def main():
    Astring=input("input it:")

    print(is_balance(Astring))
    #is_balance(Astring)

main()
