class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #map each key to the index of the key, and then the target minus the key (in tuple or list)
        #if the value in the list equals the target minus the key, and the index is different, then you've found it.

        values=[(i,target-nums[i]) for i in range(len(nums))]
        keys=[x for x in nums]
        dictionary=dict(zip(keys,values))
        print(dictionary)
        for i in range(len(nums)):
            if(target-nums[i] in dictionary):
                currentElement=dictionary[target-nums[i]]
            else:
                continue
            print(currentElement)
            if(i!=currentElement[0] and nums[i]==currentElement[1]):
                return [i,currentElement[0]]
        
        



        
      