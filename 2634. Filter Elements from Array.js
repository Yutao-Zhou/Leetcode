/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // for
    // const ans = [];
    // for (let i = 0; i < arr.length; i++) {
    //     if (fn(arr[i], i)) {
    //         ans.push(arr[i]);
    //     }
    // }
    // return ans;

    // for each
    const ans = [];
    arr.forEach((value, i) => {
        if (fn(value, i)) {
            ans.push(value);
        }
    });
    return ans;
};