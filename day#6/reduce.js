/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */

// Using User defined function

var reduce = function (nums, fn, init) {
    final_val = 0;
    if (nums.length == 0) {
        final_val = init;
        return final_val;
    }
    else {
        for (let index = 0; index < nums.length; index++) {
            if (index == 0) {
                final_val = fn(init, nums[index]);
            }
            else {
                final_val = fn(final_val, nums[index]);
            }
        }
        return final_val;
    }
};

var sum1 = function (accum, curr) {
    return accum + curr;
}

var sum2 = function (accum, curr) {
    return accum + curr * curr;
}

var sum3 = function (accum, curr) {
    return 0;
}

nums = [1, 2, 3, 4];
let testCaseI = reduce(nums, sum1, 0);
console.log(testCaseI);

let testCaseII = reduce(nums, sum2, 100);
console.log(testCaseII);

nums = [];
let testCaseIII = reduce(nums, sum3, 25);
console.log(testCaseIII);


// Using Array.reduce method

nums = [1, 2, 3, 4];
let testCaseIV = nums.reduce(sum1, 0);
console.log(testCaseIV);

nums = [1, 2, 3, 4]
let testCaseV = nums.reduce(sum2, 100);
console.log(testCaseV);

nums = [];
let testCaseVI = nums.reduce(sum3, 25);
console.log(testCaseVI);