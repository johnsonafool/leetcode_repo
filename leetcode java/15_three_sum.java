// Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

// Notice that the solution set must not contain duplicate triplets.

var threeSum = function (nums) {
    let len = nums.length;

//  return [] if the minium value is greater to 0 or the toal length of number is less than three
    if (len < 3 || Math.min(...nums) > 0) {
        return [];
    }
    let ary = [];

//  sort the list of numbers in ascending order
    nums.sort((x, y) => x - y);

//  先固定i，移動j,k縮小範圍搜尋，
//  若sum>0，k須左移，才有可能sum=0。
//  若sum<0，j須右移，才有可能sum=0。
//  若sum=0，j右移，k左移，繼續尋找下一組。
//  當j>=k時，表示這次的搜尋已結束：
    for (let i = 0; i < len - 2; i++) {
        let j = i + 1;
        let k = len - 1;
        while (j < k) {
            let sum = nums[i] + nums[j] + nums[k];
            if (sum === 0) {
                ary.push([nums[i], nums[j], nums[k]]);
//              當j或k的下一個值與現在的一樣時，就跳過，不計算：
                 while (nums[j] == nums[j + 1]) j++;
                 while (nums[k] == nums[k - 1]) k--;
                 k--;
                 j++;
             } else if (sum > 0) {
                 k--;
             } else if (sum < 0) {
                 j++;
             }
        }
    }
    return ary;
 };