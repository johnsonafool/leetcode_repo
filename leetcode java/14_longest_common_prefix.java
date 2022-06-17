// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

var longestCommonPrefix = function (strs) {
    let prefix = '';
    let strs1 = strs[0];
    let len = strs1 ? strs1.length : 0;
    for (let i = 0; i < len; i++) {
      if (strs.every(elmt => strs1[i] === elmt[i])) {
        prefix += strs1[i];
      } else {
        break;
      }
    }
    return prefix;
  };  



