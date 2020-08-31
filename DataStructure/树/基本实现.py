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


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()

    eTree =BinaryTree('')
    pStack.push