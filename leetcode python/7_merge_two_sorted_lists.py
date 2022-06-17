# we have two way to solve
# 因為效率因素，所以此題大多數都是使用迭代方式解決

from typing import Optional

#   1. recurrsive 

class Solution_recurrsive:            
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#       若 l1 為空，就沒必要比較，直接回傳 l2，反之亦然
        if l1 == None: 
            return l2;
        if l2 == None: 
            return l1;

#       判斷 input 的 l1 與 l2 第一個值誰比較大   (隨著每次呼叫自己，l1與l2會越來越短)
        if l1.val < l2.val: 
#           l1 比較小，所以 l1 第一個值留下來，把 l1.next (第二個)值 跟 l2 再執行一次自身 function
            l1.next = self.mergeTwoLists(l1.next, l2);
#           此時 return 的 l1 會是整串的，會包含 與 l2 相比，vl 這個比較小的值(第一個值)，還有 self.mergeTwoLists(l1.next, l2) 後的結果
            return l1;

        else:
            l2.next = self.mergeTwoLists(l1, l2.next);
            return l2;

#   2. iterative

class Solution_itrerative:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#       產生一個 ListNode 型態的 linked list，並且 val 裡面塞 None  (next 預設為 None)
        merge = ListNode(None)
#       用一個 pointer 指向 linked list尾端，隨著不斷 merge，將永遠指向 merge linked list 尾端來新增 node
        cursor = merge
#       若 l1 跟 l2 都不為空，則進行比較
        while l1 and l2:
#           比較 l1 跟 l2 的第一個元素 val，比較小的則加入 cursor 中，並將 後面的 linked list 覆蓋上原 linked list (所以比較小的數字會消失)
            if l1.val <= l2.val:
                cursor.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cursor.next = l2
                l2 = l2.next
            cursor = cursor.next
#       若 l2 空了，則將剩下的 l1 全部接到尾端，反之亦然
        if l1:
            cursor.next = l1
        else:
            cursor.next = l2

        return merge.next