class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix sums
        #prefix sums are helpful, allowing you to find the sum
        #of arrays in certain ranges of indices
        #to do this, create a prefix sum array with an initial index of 0
        #every element after that is the current element added to the previous element of the array
        #here, we would use prefix products.

       
        #divide by the excluded element solution (edge case for when excluded element equals 0)
        product=1
        for num in nums:
            product*=num
        result=[product for i in nums]
        #[0,0]
        for i in range(len(nums)):
            if(nums[i]!=0):
                result[i]=product//nums[i]
            else:
                result[i]=self.getProdExceptZero(nums,i)
        return result

    def getProdExceptZero(self,nums: List[int], i: int) -> int:
        resultingProd=1
        for j in range(len(nums)):
            if(j==i):
                continue
            else:
                resultingProd*=nums[j]
        return resultingProd


