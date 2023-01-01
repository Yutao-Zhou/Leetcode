/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(" ");
    let dictionary = {};
    const seen = new Set();
    if (pattern.length !== words.length){
        return false;
    };
    for (i = 0; i < words.length; i++){
        if (pattern[i] in dictionary){
            if (dictionary[pattern[i]] != words[i]){
                return false;
            };
        }else{
            if (seen.has(words[i])){
                return false;
            };
            dictionary[pattern[i]] = words[i];
            seen.add(words[i]);
        };
    };
    return true;
};