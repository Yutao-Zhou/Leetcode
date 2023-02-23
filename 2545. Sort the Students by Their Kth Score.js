/**
 * @param {number[][]} score
 * @param {number} k
 * @return {number[][]}
 */
var sortTheStudents = function(score, k) {
    /** Bubble Sort */ 
    // for (let j = score.length - 1; j > 0; j--){
    //     for (let i = 1; i <= j; i++){
    //         if (score[i][k] > score[i - 1][k]){
    //             let s = score[i]
    //             score[i] = score[i - 1]
    //             score[i - 1] = s
    //         } 
    //     }
    // }
    // return score

    /** JavaScript Sort */ 
    score.sort((a, b) => b[k] - a[k]);
    return score;
};