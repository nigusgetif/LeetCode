class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
            elif (s[i] == ']' or s[i] == '}' or s[i] == ')') and len(stack)== 0 :
                return False
            elif s[i] == '}':   
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False       
            elif stack and s[i] == ']':    
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False       
            elif s[i] == ')':    
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False    
        if len(stack)== 0:           

           return True

        