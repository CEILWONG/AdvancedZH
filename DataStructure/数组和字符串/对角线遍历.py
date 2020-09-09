class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        outlist=[]

        m=len(matrix)
        if m==0:
            return outlist
        n=len(matrix[0])
        if n==0:
            return
        if m==0 and n==1:
            outlist.append(matrix[0][0])
            return outlist


        for num in range(m+n-1):
            if num%2==0:#m减小()，n增大

                bigm= num if num<m-1 else m-1
                while bigm>-1 and num-bigm<n:
                    outlist.append(matrix[bigm][num-bigm])
                    bigm-=1
            else:
                bign=num if num<n-1 else n-1
                while bign>-1 and num-bign<m:
                    outlist.append(matrix[num-bign][bign])
                    bign-=1

        return outlist
