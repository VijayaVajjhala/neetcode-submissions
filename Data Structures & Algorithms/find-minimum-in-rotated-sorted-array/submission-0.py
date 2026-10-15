class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2

        while low < high:
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid
            mid = (low + high) // 2

        return nums[low]