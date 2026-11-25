class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #run a binary search on both sides of the array?
        #if the sum is greater than the target, subtract 1 from right
        #if the sum is less than the target, add 1 to left
        #two pointer approach

        left=0
        right=len(numbers)-1
        while(left<right):
            sum=numbers[left]+numbers[right]
            if(sum==target):
                return [left+1,right+1]
            elif(sum>target):
                right-=1
            elif(sum<target):
                left+=1



        #5 8 9 10 14 
        #target = 23
        #19<target, left+=1
        #22<target, left+=1
        #23==target!