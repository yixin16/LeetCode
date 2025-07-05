class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = 0
        lucky_num = []
        for i in range(len(arr)):
            if arr.count(arr[i]) == arr[i]:
                lucky_num.append(arr[i])
        
        if len(lucky_num) == 0:
            return -1
        return max(lucky_num)
        