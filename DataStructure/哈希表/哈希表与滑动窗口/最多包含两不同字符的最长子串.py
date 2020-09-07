class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        def num_notzero(hashlist):
            num=0
            for key in hashlist:
                if hashlist[key]!=0:
                    num+=1
            return num

        length=len(s)
        if length<3:
            return length

        hashtable={}
        left=0
        maxlen=0

        for right in range(length):
            if s[right] not in hashtable:
                hashtable[s[right]]=0

            hashtable[s[right]]+=1
            num=num_notzero(hashtable)
            if num>2:
                hashtable[s[left]]-=1
                left+=1
            else:
                maxlen=right-left+1 if right-left+1>maxlen else maxlen

        return maxlen