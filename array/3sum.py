class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()

        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add((nums[i], nums[j], nums[k]))

        return list(result)
