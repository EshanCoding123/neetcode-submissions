class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #represent this as one sorted array.
        rowIndex=None
        for row in range (len(matrix)):
            if(target>=matrix[row][0] and target<=matrix[row][len(matrix[row])-1] and rowIndex==None):
                rowIndex=row
        print('here')
        if(rowIndex==None):
            return False
        #do binary search on that row
        searchRow=matrix[rowIndex]
        low=0
        high=len(searchRow)-1
        while(low<=high):
            mid=(low+high)//2
            if(searchRow[mid]==target):
                return True
            elif(target<searchRow[mid]):
                high=mid-1
            elif(target>searchRow[mid]):
                low=mid+1

        return False