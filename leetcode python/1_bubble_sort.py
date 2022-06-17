from typing import List

nums = [1, 3, 2, 9, 4]

class Solution(nums):
    def sortArray(self, nums:List[int]) -> List[int]:
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    t = nums[j]
                    nums[j] = nums[j+1]
                    nums[j] = t
        return nums
        
Solution(nums)

print(Solution)