class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        #racecar, carrace
        keys1={f"{l}" for l in s} #r, a, c, e
        values1=[[] for key in keys1]
        keys2={f"{l}" for l in t} #c, a, r, e
        values2=[[] for key in keys2]
        if(keys1!=keys2):
            return False
        keys1=list(keys1)
        keys2=list(keys2)
        map1=dict(zip(keys1,values1))
        map2=dict(zip(keys2,values2))
        for value in s:
            map1[value].append(value)
        for value in t:
            map2[value].append(value)
        if(map1!=map2):
            return False
        return True
        
        


