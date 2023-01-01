/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if (s.length !== t.length){
        return false;
    };
    let dictionary = {};
    let seen = new Set();
    for (i = 0; i < s.length; i++){
        if (s[i] in dictionary){
            if (dictionary[s[i]] !== t[i]){
                return false;
            };
        }else{
            if (seen.has(t[i])){
                return false;
            };
            dictionary[s[i]] = t[i];
            seen.add(t[i]);            
        };
    };
    return true;
};