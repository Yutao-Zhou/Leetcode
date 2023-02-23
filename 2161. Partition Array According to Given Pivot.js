/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    /** Brute Force Create and concat */
    // let less = [];
    // let equal = [];
    // let larger = [];
    // for (let i = 0; i < nums.length; i++) {
    //     if (nums[i] < pivot){
    //         less.push(nums[i]);
    //     } else if (nums[i] > pivot) {
    //         larger.push(nums[i]);
    //     } else {
    //         equal.push(nums[i]);
    //     }
    // }
    // return less.concat(equal, larger);

    /** Modified Insert Sort */
    let less = 0;
    let equal = 0;
    let larger = 0;
    let ans = new Array(nums.length);
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < pivot){
            less++;
        } else if (nums[i] > pivot) {
            larger++;
        } else {
            equal++;
        }
    }
    let left = 0;
    let middle = less;
    let right = less + equal;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < pivot){
            ans[left] = nums[i];
            left++;
        } else if (nums[i] > pivot) {
            ans[right] = nums[i];
            right++;
        } else {
            ans[middle] = nums[i];
            middle++;
        }
    }
    return ans;
};