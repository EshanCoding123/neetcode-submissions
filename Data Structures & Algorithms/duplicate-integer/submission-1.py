class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums=[1,2,3,3]
        keys = {f"{nums[i]}" for i in range(len(nums))}#[1,2,3]
        keys=list(keys)
        values=[[] for key in keys] #[[],[],[]]
        map = dict(zip(keys,values))
        for i in range(len(nums)):
            map[f"{nums[i]}"].append(nums[i])
        for num in nums:
            if(len(map[f"{num}"])>1):
                return True
        return False
        
        
            
            
      