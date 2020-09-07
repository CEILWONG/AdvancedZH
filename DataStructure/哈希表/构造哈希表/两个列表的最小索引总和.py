class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        outlist=[]

        hashmap={}

        for i in range(len(list1)):
            if list1[i] not in hashmap:
                hashmap[list1[i]]=i
            else:
                pass

        min=2000
        for i in range(len(list2)):
            name=list2[i]
            if name in hashmap:
                hashmap[name]=hashmap[name]+i
                if hashmap[name]<min:
                    outlist=[name,]
                    min=hashmap[name]
                elif hashmap[name]==min:
                    outlist.append(name)
                else:
                    pass
        return outlist

