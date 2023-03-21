/**
 * @param {number[]} nums
 * @return {number[]}
 */
var maxScoreIndices = function(nums) {
    /** Brute Force simulation O(n ** 2) */
    // let ans = [],
    //     maximum = 0,
    //     score = 0;
    // for (i = 0; i <= nums.length; i++) {
    //     score = 0;
    //     for (l = 0; l < i; l++) {
    //         if (nums[l] === 0) {
    //             score += 1;
    //         }
    //     }
    //     for (r = i; r < nums.length; r++) {
    //         if (nums[r] === 1) {
    //             score += 1;
    //         }
    //     }
    //     if (score === maximum) {
    //         ans.push(i);
    //     } else if (score > maximum) {
    //         maximum = score;
    //         ans = [i];
    //     }
    // }
    // return ans;
    /** Two pass */
    let ones = 0;
    for (i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            ones += 1;
        }
    }
    let score = ones,
        zeros = 0,
        ans = [0];
    for (i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            zeros += 1;
        };
        if (zeros + (ones - (i - zeros + 1)) > score) {
            score = zeros + (ones - (i - zeros + 1));
            ans = [i + 1];
        } else if (zeros + (ones - (i - zeros + 1)) === score) {
            ans.push(i + 1);
        }
    }
    return ans;
};