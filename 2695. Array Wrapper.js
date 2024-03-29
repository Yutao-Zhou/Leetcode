/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.nums = nums
};

ArrayWrapper.prototype.valueOf = function() {
    let s = 0;
    for (let i = 0; i < this.nums.length; i++) {
        s += this.nums[i];
    }
    return s;
}

ArrayWrapper.prototype.toString = function() {
    let result = '[';
    for (let i = 0; i < this.nums.length; i++) {
        result += this.nums[i]
        if (i !== this.nums.length - 1) {
            result += ','
        }
    }
    return result + ']';
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */