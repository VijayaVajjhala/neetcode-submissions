from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1 = defaultdict(int)
        rightpos = 0
        leftpos = 0
        maxf = 0
        maxlen = 0

        for i,c in enumerate(s):
            rightpos = i            
            dict1[c] += 1
            maxf = max(dict1.values())

            while (rightpos - leftpos + 1) - maxf > k:
                dict1[s[leftpos]] -= 1
                leftpos += 1
            maxlen = max(maxlen,(rightpos - leftpos +1))

        return maxlen

#AABABBA  == 4
        