class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            max_val = float('-inf')
            pos = -1
            for j in range(len(nums)):
                if nums[j] > max_val:
                    max_val = nums[j]
                    pos = j
            
            nums[pos] = float('-inf')
        
        return max_val
            

