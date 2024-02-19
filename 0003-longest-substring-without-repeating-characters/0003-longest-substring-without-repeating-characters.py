class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        maxlen = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in char_index:
                start = max(start, char_index[s[i]] + 1)
            char_index[s[i]] = i
            maxlen = max(maxlen, i - start + 1)
            
        return maxlen    
                