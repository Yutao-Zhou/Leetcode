/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // check key length
    // return Object.keys(obj).length === 0;
    
    // stringify
    // return JSON.stringify(obj).length <= 2;
    
    //loop
    for (const _ in obj) {
        return false;
    } 
    return true;
};