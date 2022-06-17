// Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

var removeDuplicates = function(nums) {
    let i = 0;
    for (i; i < nums.length; i++) {
        if (nums[i] === nums[i + 1]) {
            nums.splice(i + 1, 1);
            i--;
        }
    }
    return i;
};

