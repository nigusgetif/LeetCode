class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        converted_str = str(abs(x))
        
        reversed_str  = "".join(reversed(converted_str)) 
        
        reversed_int = int(reversed_str)
        
        if is_negative:
            reversed_int = -reversed_int
            
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            
             return 0
            
        return reversed_int
        
        