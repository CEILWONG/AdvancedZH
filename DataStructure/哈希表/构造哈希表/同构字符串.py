class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1={}
        hashmap2={}
        for i in range(len(s)):
            if t[i] not in hashmap1:
                hashmap1[t[i]]=s[i]
            else:
                if hashmap1[t[i]]!=s[i]:
                    return False

            if s[i] not in hashmap2:
                hashmap2[s[i]]=t[i]
            else:
                if hashmap2[s[i]]!=t[i]
                    return False

        return True
