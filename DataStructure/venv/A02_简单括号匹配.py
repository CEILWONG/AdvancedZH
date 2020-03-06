#简单括号匹配的意思，用来判断一个字符串，这个字符串里面只有括号符号，我们需要编写代码来判断是否左右括号匹配；
#简单版的应该是只有（），复杂版的则是既有（），又有[],{};

#应用：HTML或者爬虫语言中，上下文的组队括号，就用到栈的用法；

#判断字符串中的括号是否平衡



class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,x):
        self.item.append(x)

    def pop(self):
        self.item=self.item[0:len(self.item)-1]

    def length(self):
        return len(self.item)


def is_balance(Astring):
    s=Stack()

    for x in Astring:
        if x == "(":
            s.push(x)
        elif x==")":
            if s.length()==0:
                return "not balance"
            else:
                s.pop()
        else:
            return "there's other word"

    if s.length() == 0:
        return "yes,balance"
    else:
        return "not balance"


def main():
    Astring=input("input it:")

    print(is_balance(Astring))
    #is_balance(Astring)

main()