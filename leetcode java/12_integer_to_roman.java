// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

var intToRoman = function(num) {
    let val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
    let romNum = '';
    let len = val.length;
    for (let i = 0; i < len; i++) {
      if (num >= val[i]) {
        let count = parseInt(num / val[i]);
        num = num % val[i];
        romNum += roman[i].repeat(count);
      }
    }
    return romNum;
  };var intToRoman