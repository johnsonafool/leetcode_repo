// Given a 32-bit signed integer, reverse digits of an integer.

var reverse = function(x) {
    let maxValue = Math.pow(2, 31) - 1;
    let v = +Array.from('' + Math.abs(x)).reverse().join('');
    let v2 = x < 0 ? v * - 1 : v;
    let v3 = (-1 * maxValue - 1 <= v && v <= maxValue) ? v2 : 0;
    return v3;
  };
