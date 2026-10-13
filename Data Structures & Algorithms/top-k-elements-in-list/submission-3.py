from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap with the element, and the number of elements in the list corresponding to that element
        #sort all of the keys
        keys={i for i in nums}
        keys=list(keys)
        values=[0 for key in keys]
        frequencies=dict(zip(keys,values))
        for element in nums:
            frequencies[element]+=1
        frequencies = dict(sorted(frequencies.items(), key=itemgetter(1)))
        #1: 1, 2: 2, 3: 3
        result=[]
        i=len(keys)-1 #2
        count=0 
        sortedKeysList=list(frequencies.keys())
        print(sortedKeysList)
        while(count<k): #k=2
            result.append(sortedKeysList[i])
            i-=1
            count+=1
        return result
        #1:1 2:2 3:3
        