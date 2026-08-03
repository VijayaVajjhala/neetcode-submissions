import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        left = 1
        right = maxk
        while left <= right:
            mid = (right + left) //2
            times = self.eatBananas(piles,mid)
            if times <= h:
                right = mid - 1
            elif times > h:
                left = mid + 1
        return left

    def eatBananas(self,piles,val):
        times = 0
        for pile in piles:
            times += math.ceil(pile/val)
        return times


        





        