// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// An input string is valid if:
// Open brackets must be closed by the same type of brackets.
//Open brackets must be closed in the correct order.

// Solving by "Stack", "LIFO (last in first out)"

let isValid = function (s) {
    if (!s) return true;
  
    let stack = [];
  
    let left = ['(', '[', '{'];
    let right = [')', ']', '}'];
    let match = {
      ')': '(',
      ']': '[',
      '}': '{'
    }
  
    for (let i in s) {
      if (left.indexOf(s[i]) > -1) {
        stack.push(s[i]);
      }
  
      if (right.indexOf(s[i]) > -1) {
        let stackStr = stack.pop();
        if (match[s[i]] != stackStr) {
          return false;
        }
      }
    }
    return stack.length == 0;
  };

  