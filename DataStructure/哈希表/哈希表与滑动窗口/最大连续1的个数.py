class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:


        hashtable={}
        hashtable[0]=0
        hashtable[1]=0
        maxlen=0
        left = 0
        for right in range(len(A)):
            hashtable[A[right]]+=1

            #

            while hashtable[0]>K:
                hashtable[A[left]]-=1
                left+=1
            else:
                windows_length = right - left + 1
                maxlen = windows_length if windows_length > maxlen else maxlen
        return maxlen

