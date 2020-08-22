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

def isBrakectsMatch(givenstr):
    s=Stack()
    LeftBrakects=['<','(','[','{']
    RightBrakects=['>',')',']','}']
    for i in givenstr:
        if i in LeftBrakects:
            s.push(i)
        elif i in RightBrakects:
            if s.size()==0:
                return False
            else:
                if LeftBrakects.index(s.pop())!=RightBrakects.index(i):
                    return False
                else:
                    pass
        else:
            pass

    if s.size() == 0:
        return True
    else:
        return False


wzhstr="()[]45fved{<>}}"

print(isBrakectsMatch(wzhstr))

874906754