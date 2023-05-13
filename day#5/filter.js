/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

// Using User defined function 

var filter = function (arr, fn) {
    newarr = [];
    for (let index = 0; index < arr.length; index++) {
        if (fn(arr[index], index)) {
            newarr.push(arr[index])
        }
    }
    return newarr;
};

var graterThan10 = function (n, i) {
    return n > 10;
}

var firstIndex = function (n, i) {
    return i === 0;
}

var plusOne = function (n, i) {
    return n + 1;
}

arr = [0, 10, 20, 30];
let testCaseI = filter(arr, graterThan10);
console.log(testCaseI);

arr = [1, 2, 3];
let testCaseII = filter(arr, firstIndex);
console.log(testCaseII);

arr = [-2, -1, 0, 1, 2]
let testCaseIII = filter(arr, plusOne);
console.log(testCaseIII);