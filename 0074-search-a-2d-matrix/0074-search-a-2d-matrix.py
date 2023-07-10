class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = len(matrix)-1
        for i in range(0,len(matrix)): #number of rows
            if matrix[i][0]==target:
                return True
            elif matrix[i][0]>target:
                target_row = i-1
                break
            else:
                continue
                
    
        for i in range(0,len(matrix[0])): #number of columns
            if matrix[target_row][i]==target:
                return True
        
        return False
        