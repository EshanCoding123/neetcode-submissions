class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        result=""
        for letter in s.lower():
            if(letter.isdigit()):
                result+=letter
            elif(letter.isalpha()):
                result+=letter
        print(result)
        left=0
        right=len(result)-1
        while(left<=right):
            if(left==right):
                return True
            elif(result[left]!=result[right]):
                return False
            else:
                left+=1
                right-=1
        return True