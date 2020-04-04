'''

字典是key-value的键值对数据类型

这种键值关联的方法叫做映射 MAP

ADT Map的结构就是键值关联的无序集合
'''

#实现一个hashtable来实现这个键值，用两个列表，一个是slot存放key，一个是data存放value

class HashTable(object):
    def __init__(self):

        self.size=17
        self.slot=[None]*self.size
        self.data=[None]*self.size

    def put(self,key,value):

        hashvalue=key%self.size

        if slot[hashvalue] == None:
            slot[hashvalue] = key
            data[hashvalue] = value

        else:
            if slot[hashvalue] == None:
                data[hashvalue] = value
            else:
                nextslot = (hashvalue+1)%self.size
                while slot[nextslot] != None and slot[nextslot] != key:
                    nextslot = (nextslot+1)%self.size

                slot[nextslot] = key
                date[nextslot] = value

    def get(self,key):
        


