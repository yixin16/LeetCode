class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start, stop = i + 1, n - 1
            target = -nums[i]

            while start < stop:
                total = nums[start] + nums[stop]

                if total < target:
                    start += 1
                elif total > target:
                    stop -= 1
                else:
                    result.append([nums[i], nums[start], nums[stop]])

                    start += 1
                    stop -= 1

                    while start < stop and nums[start] == nums[start - 1]:
                        start += 1
                    while start < stop and nums[stop] == nums[stop + 1]:
                        stop -= 1

        return result
