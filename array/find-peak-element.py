class Solution:
    def findPeakElement(self, nums):
        pos = nums.index(max(nums))
        return pos