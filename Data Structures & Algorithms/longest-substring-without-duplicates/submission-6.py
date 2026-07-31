from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        leftpos = 0
        rightpos = 0
        maxlen = 0

        for i,char in enumerate(s):
            rightpos = i
            if char in seen:
                while s[rightpos] in seen:
                    seen.remove(s[leftpos])
                    leftpos += 1
            maxlen = max(maxlen,rightpos - leftpos + 1)
            seen.add(char)
            
        return maxlen

#dvdd


        