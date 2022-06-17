// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

var isPalindrome = function(x) {
    if (x < 0) {
    return false;
  }
  let div = 1;
  while (x / div >= 10) {
    div *= 10;
  }
  
  while (div > 1) {
    if (Math.floor(x / div) === x % 10) {
      div /= 10;
      x = Math.floor(x / 10) % div;
      div /= 10;
      continue;
    } else {
      return false;
    }
  }
  return true;
  };

  // var isPalindrome = function(x) {
  //   if (x < 0) {
  //   return false;
  // }
  // let div = 1;
  // while (x / div >= 10) {
  //   div *= 10;
  // }
  
  // while (div > 1) {
  //   if (Math.floor(x / div) === x % 10) {
  //     div /= 10;
  //     x = Math.floor(x / 10) % div;
  //     div /= 10;
  //     continue;
  //   } else {
  //     return false;
  //   }
  // }
  // return true;
  // };

// var iamJohn = function(y){

// }
