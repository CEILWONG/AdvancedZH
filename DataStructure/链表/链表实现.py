
class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self,idata):
        self.data=idata

    def setnext(self,newnext):
        self.next=newnext


class UnorderedList:
    def __init__(self):
        self.head=None

    def add(self,item):
        atemp=Node(item)
        atemp.setnext(self.head)
        self.head=atemp

    def size(self):
        num=0
        temp=self.head
        while temp!=None:
            num=num+1
            temp=temp.getnext()
        return num

    def showTheList(self):
        outlist=[]

        temp=self.head
        while temp!=None:
            outlist.append(temp.getdata())
            temp=temp.getnext()
        return outlist

    def search(self,item):
        current=self.head
        found=False

        while current!=None and not found:
            if current.getdata()==item:
                found=True
            else:
                current=current.getnext()
        return found

    def remove(self,item):
        current = self.head
        previous=None
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                previous=current
                current = current.getnext()

        if not found:
            print("not exist")
        elif previous==None:
            self.head=current.getnext()
        else:
            previous.setnext(current.getnext())



atmp=Node(20)

#print(atmp.getdata())
#print(atmp.getnext())

aList=UnorderedList()
aList.add(2)
aList.add(3)
aList.add(7)
aList.add(9)
aList.add(10)

#print(aList.size())

print(aList.showTheList())

aList.remove(7)
print(aList.showTheList())

#print(aList.search(1))
#print(aList.search(2))