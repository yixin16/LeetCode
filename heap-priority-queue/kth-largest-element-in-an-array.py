import random

class Solution:
    def findKthLargest(self, nums, k):
        k -= 1
        left, right = 0, len(nums) - 1

        while True:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store = left
            for i in range(left, right):
                if nums[i] > pivot:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1

            nums[store], nums[right] = nums[right], nums[store]

            if store == k:
                return nums[store]
            elif store < k:
                left = store + 1
            else:
                right = store - 1
