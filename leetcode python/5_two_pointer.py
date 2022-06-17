# Two pointer 

from typing import List

## Psudocode
# 1. let two pointer k, j
# 2. start k from number two
# 3. compare each number it met with previous one -> same or not same
# 4.    if same: remove the same number
#       else: return j + 1 and repeat 3.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#       k 會用來計算不重複元素的位置
        k = 1
#       j 會走得比較快，把不重複的值，丟給 k 位置儲存
        for j in range(1, len(nums)):
#           判斷第 j 個位置跟第 j-1 的位置，是否不相等，若不相等，就把 nums[k] 儲存 nums[j]，並 k 向右移動
            if nums[j] != nums[j - 1]:
                nums[k] = nums[j]
                k += 1

        return k


