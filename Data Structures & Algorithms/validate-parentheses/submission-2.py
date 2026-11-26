class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2!=0):
            return False
        
        #[], {}, or ()
        #add open brackets to the stack
        #if its a closed bracket, remove the corresponding open bracket if its in the list, otherwise return false (because that means a closed bracket is occurring before an open one)
        #a bracket is closed, but the most recent open one is not the same type, return false
        stack=[]
        for bracket in s:
            if(bracket=="{" or bracket=="[" or bracket=="("):
                stack.append(bracket)
            elif(bracket=="}"):
                if(len(stack)==0 or stack[-1]!="{"):
                    return False
                else:
                    stack.pop()
            elif(bracket==")"):
                if(len(stack)==0 or stack[-1]!="("):
                    return False
                else:
                    stack.pop()
            elif(bracket=="]"):
                if(len(stack)==0 or stack[-1]!="["):
                    return False
                else:
                    stack.pop()
        return True if len(stack)==0 else False


                