#Hoare

from typing import List

class Solution: 
    def sortArray(self, nums: List[int]) -> List[int]:
#       先判斷 nums 有無資料
        if not nums:
            return
#       開始 Quick Sort 的 Hoare 方法
        self.QuickSort_Hoare(nums, 0 , len(nums) - 1)
        return nums
        
    def QuickSort_Hoare(self, nums, start, end):
#       把 start ~ end 之間要進行排序
        if start >= end: 
            return
#       有兩個指標，k 從左邊往右，j 從右邊往左
        k, j = start, end
#       pivot 為中位數
        pivot = nums[(start + end) // 2]
        
#       當 k 與 j 會逐漸靠近，直到 k > j
        while k <= j:
#           在 k 與 j 還沒相遇的情況，k 會一直往右，直到停在比 pivot 大的位置 
            while k <= j and nums[k] < pivot:
                k += 1

#           在 k 與 j 還沒相遇的情況，j 會一直往左，直到停在比 pivot 小的位置 
            while k <= j and nums[j] > pivot:
                j -= 1     
#           在 k 與 j 還沒相遇的情況，此時 k 停在比 pivot 大的位置，j 停在比 pivot 小的位置，將兩者的值互換，並且兩個互相接近一個位置             
            if k <= j:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1
                j -= 1
            # print(nums)    
#       當 k 與 j 相遇後，位置也排完，此時 k > j，那麼 start~j 是 左邊比 pivot 小的，k ~ end 是 右邊比 pivot 大的 
        self.QuickSort_Hoare(nums, start, j)
        self.QuickSort_Hoare(nums, k, end)