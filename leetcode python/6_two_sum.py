from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while not numbers[left] + numbers[right] == target:
            while numbers[left] + numbers[right] > target and left != right:
                right -= 1 
            while numbers[left] + numbers[right] < target and left != right:
                left += 1

        return [left+1,right+1]
