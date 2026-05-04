class Solution(object):
    def rotate(self, matrix):
        l=len(matrix)
        l1=len(matrix[0])
        for i in range(0,l-1):
            for j in range(i+1,l):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
            i.reverse()
        return matrix
        
