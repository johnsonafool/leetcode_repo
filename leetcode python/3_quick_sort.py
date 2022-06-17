#Lomuto

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.QuickSort_Lomuto(0, len(nums))
        return nums
    
    def QuickSort_Lomuto(self, left: int, right: int) -> None:
        nums = self.nums
        
        # End Condition
        if left >= right: return

        # Partition
        i, j, pivot = left, left, (left + right) // 2

        # Sort
        while(i < right and j < right):
            # When the loop stoped, nums[i] >= nums[pivot]
            while(i < right and nums[i] < nums[pivot]): i += 1

            # When the loop stoped, nums[j] < nums[pivot]
            if j < i: j = i
            while(j < right and nums[j] >= nums[pivot]): j += 1

            if i < j and j < right:
                # Swap
                nums[i], nums[j] = nums[j], nums[i]
                if i == pivot: pivot = j
                    
                # Move on
                i += 1
                j += 1
				# Put pivot to the correct location
        nums[i], nums[pivot] = nums[pivot], nums[i]

		# Recursion
        self.QuickSort_Lomuto(left, i)
        self.QuickSort_Lomuto(i + 1, right)