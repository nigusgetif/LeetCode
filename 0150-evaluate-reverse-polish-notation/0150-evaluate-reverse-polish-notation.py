class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
          stack = []
          set = {'+','*','-',"/"}
          for i in range (len(tokens)):
              if tokens[i] not in set:
                  stack.append(int(tokens[i]))
              else:
                  n1 = stack.pop()
                  n2 = stack.pop()
                  if tokens[i] == '+':
                      stack.append(n1 + n2)  
                  elif tokens[i] == '-':
                      stack.append((n2 - n1))      
                  elif tokens[i] == '*':
                      stack.append(n2 * n1)   
                  elif tokens[i] == '/':
                      stack.append(int(n2 / n1))  

          if len(stack) == 1:
              return stack[0]                   
