/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // loop 
    // let ans = [];
    // for (let i = 0; i < arr.length; i++) {
    //     ans[i] = fn(arr[i], i);
    // }
    // return ans;

    // no extra space
    for (let i = 0; i < arr.length; i++) {
        arr[i] = fn(arr[i], i);
    }
    return arr;
};