class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = [[0,0] for i in range(2001)]
        result = []

        for num in nums:
            count_freq[num+1000][1] = num
            count_freq[num + 1000][0] += 1

        count_freq.sort()
        print(count_freq)

        i = k

        while i > 0:
            result.append(count_freq[len(count_freq)-i][1])
            i -= 1

        return result



        

        
        