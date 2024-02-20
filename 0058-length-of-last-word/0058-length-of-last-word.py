class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        maxLength = 0
        for char in reversed(s):
          if char.isalpha():
            maxLength += 1
          elif maxLength > 0:
            break
        return maxLength    
          
            
            