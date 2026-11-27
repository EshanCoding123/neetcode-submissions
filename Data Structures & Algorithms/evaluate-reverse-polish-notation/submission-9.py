
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for value in tokens:
            try:
                val=int(value)
                stack.append(val)
            except ValueError:
                #print(stack)
                top1=stack.pop()
                top2=stack.pop()
                if(value=="+"):
                    stack.append(top2+top1)
                elif(value=='-'):
                    stack.append(top2-top1)
                elif(value=='*'):
                    stack.append(top2*top1)
                elif(value=='/'):
                    stack.append(int(top2/top1))

        return stack[0]
