/**
 * @param {string[]} garbage
 * @param {number[]} travel
 * @return {number}
 */
var garbageCollection = function(garbage, travel) {
    /** Simulation three pass */
    let ans = 0;
    let type = ["M", "P", "G"];
    for (let j = 0; j < 3; j++) {
        let distance = 0;
        for (let i = 0; i < garbage.length; i++) {
            if (i !== 0) {
                distance += travel[i - 1];
                ans += travel[i - 1];
            }
            for (let c = 0; c < garbage[i].length; c++) {
                if (garbage[i][c] === type[j]) {
                    ans += 1;
                    distance = 0;
                }
            }
        }
        ans -= distance;
    }
    return ans;
};