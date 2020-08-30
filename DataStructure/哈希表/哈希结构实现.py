

class HashTable:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def hashfunction(self,key):#根据key值选一个位置
        return key%self.size

    def rehash(self,hashvalue):#如果第一次没找到合适的，用rehash函数再找下一个可用的位置
        return (hashvalue+1)%self.size

    def put(self,key,value):
        hashvalue=self.hashfunction(key)
        if self.slots[hashvalue]==None or self.slots[hashvalue]==key:
            self.slots[hashvalue]=key
            self.data[hashvalue]=value
        else:
            nextslot=self.rehash(hashvlaue)
            while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                nextslot=self.rehash(nextslot)

            self.slots[nextslot]=key
            self.data[nextslot]=value

    def get(self,key):
        hashvalue=self.hashfunction(key)

        if self.slots[hashvalue]==key:
            return self.data[hashvalue]
        else:
            times=1
            nextslot=self.rehash(hashvalue)
            while self.slots[nextslot]!=None and self.slots[nextslot]!=key and times<12:
                nextslot=self.rehash(nextslot)
                times+=1

            if self.slots[nextslot]==None:
                return False
            else:
                return self.data[nextslot]


    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key,value)


'''
    def put(self,key,value):
        hashvalue=self.hashfunction(key)

        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=value
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=value
            else:
                nextslot=self.rehash(hashvalue)
                while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=value
                else:
                    self.data[nextslot]=value
'''

hslist=HashTable(10)
hslist.put(3,'wa')
print(hslist.slots)
print(hslist.data)
print(hslist.get(3))

hs=HashTable(11)
hs[103]='wa'
print(hs[103])
