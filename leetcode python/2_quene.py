class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
#       分別宣告兩個 stack，命名為 stack1 與 stack2
#       stack1 放存進來的值
#       stack2 是把 stack1 的值逐一放入stack2，變成 Queue 的形式(最早放的會在最上面)
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
#       呼叫 push function 時，會把變數 x 放進 stack1 中
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
#       呼叫 pop function 時，要拿出最早放入的值，所以先看看 stack2 有沒有值 ( stack2 是已經變成 Queue 排列的順序)
#       stack2 若是空的，就把 stack1 的值逐一放入 stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
#       回傳 stack2 最上面的值
        return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
#       跟上面 pop function 一樣，判斷stack2 是不是空的，若是空的，就把 stack1 的值逐一放入 stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
#       由於是 peek，只會看最前面是什麼，不會把值拿出來，所以拿出來後還要儲存回去        
        top = self.stack2.pop()
        self.stack2.append(top)
        return top

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
#       檢查 stack1 跟 stack2 是不是空的
        if self.stack1 or self.stack2:
            return False
        else:
            return True

