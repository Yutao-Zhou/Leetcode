/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort(function(a, b) {return a - b});
    let ans = 0,
        l = 0,
        r = piles.length - 1;
    for(l; l < r; l++) {
        ans += piles[r - 1];
        r -= 2;
    };
    return ans;
};