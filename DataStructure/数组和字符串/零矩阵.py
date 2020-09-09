class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        setm=set()
        setn=set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    setm.add(i)
                    setn.add(j)

        for i in range(m):
            for j in range(n):
                if i in setm or j in setn:
                    matrix[i][j]=0
