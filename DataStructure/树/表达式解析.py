class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.left=None
        self.right=None

    def insertLeft(self,newObj):
        if self.left==None:
            self.left=BinaryTree(newObj)
        else:
            t=BinaryTree(newObj)
            t.left=self.left
            self.left=t


    def insertRight(self,newObj):
        if self.right==None:
            self.right=BinaryTree(newObj)
        else:
            t=BinaryTree(newObj)
            t.right=self.right
            self.right=t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootObj(self,obj):
        self.key=obj

    def getRootObj(self):
        return self.key

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


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()

    eTree =BinaryTree('')
    pStack.push(eTree)

    currentTree=eTree

    for i in fplist:
        if i=='(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeft()
        elif i not in ['+','-','*','/',')']
            currentTree.setRootObj(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in ['+','-','*','/']:
            currentTree.setRootObj(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRight()
        elif i == ')':
            currentTree=pStack.pop()
        else:
            raise ValueError

    return eTree

def preoder(tree):
    if tree:
        print(tree.getRootObj)
        preoder(tree.getLeft())
        preoder(tree.getRight())

def postorder(tree):
    if tree:
        postorder(tree.getLeft)
        postorder(tree.getRight)
        print(tree.getRootObj)

def inorder(tree):
    if tree:
        inorder(tree.getLeft)
        print(tree.getRootObj)
        inorder(tree.getRight)

