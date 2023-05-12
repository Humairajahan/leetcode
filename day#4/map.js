var plusone = function (n, i) {
    return n + 1;
}

var plusI = function (n, i) {
    return n + i;
}

var constant = function (n, i) {
    return 42;
}

var map = function (arr, fn) {
    newarr = [];
    for (let index = 0; index < arr.length; index++) {
        newarr.push(fn(arr[index], index));
    }
    return newarr;
};

arr = [1, 2, 3];
const testCaseI = map(arr, plusone);
console.log(testCaseI);

const testCaseII = map(arr, plusI);
console.log(testCaseII);

arr = [10, 20, 30];
const testCaseIII = map(arr, constant);
console.log(testCaseIII);
