class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #monotonic-> binary search

        #find row:

        l =0
        r=len(matrix)-1
        row = 0
        while l<=r:
            mid = l + (r-l)//2
            if target > matrix[mid][-1]:
                l = mid+1
            elif target< matrix[mid][0]:
                r = mid-1
            else:
                row = mid
                break #within that row
        
        if not (l<=r):
            return False #not there- pointers crossed

        left,right = 0, len(matrix[0])-1

        while left<= right:
            mid = left + (right-left)//2
            if target > matrix[row][mid]:
                left = mid+1
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                return True
        return False
    #can flatten into one array but extra space and time
