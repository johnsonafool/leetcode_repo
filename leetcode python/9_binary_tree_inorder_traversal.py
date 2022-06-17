from typing import Optional, List


class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(node):
            if node == None:
                return None

            traverse(node.left)
            ans.append(node.val)    
            traverse(node.right)

        traverse(root)
        return ans


#iterative
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
#       當 root 與 stack 都為空，代表走訪完整個二元樹
        while root or stack:
#           不斷走訪左child，直到樹的最左下角，每次走訪都存入 stack 中
            while root:
                stack.append(root)
                root = root.left
#           將儲存在 stack 的資料拿出來
            root = stack.pop()
#           ans 儲存 root.val
            ans.append(root.val)
#           換走訪 root 的 右 child 
            root = root.right
        return ans

