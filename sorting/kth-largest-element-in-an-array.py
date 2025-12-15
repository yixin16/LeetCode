import random

class Solution:
    def findKthLargest(self, nums, k):
        k = k - 1  # 第 k 大 → index k-1

        def quickselect(left, right):
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # 把 pivot 移到末尾
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if nums[i] > pivot: 
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            if store_idx == k:
                return nums[store_idx]
            elif store_idx > k:
                return quickselect(left, store_idx - 1)
            else:
                return quickselect(store_idx + 1, right)

        return quickselect(0, len(nums) - 1)
