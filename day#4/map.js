var plusone = function (n, i) {
    return n + 1;
}

var plusI = function (n, i) {
    return n + i;
}

var constant = function (n, i) {
    return 42;
}

// Using User defined function

var map = function (arr, fn) {
    newarr = [];
    for (let index = 0; index < arr.length; index++) {
        newarr.push(fn(arr[index], index));
    }
    return newarr;
};


arr = [1, 2, 3];
let testCaseI = map(arr, plusone);
console.log(testCaseI);

let testCaseII = map(arr, plusI);
console.log(testCaseII);

arr = [10, 20, 30];
let testCaseIII = map(arr, constant);
console.log(testCaseIII);



// Using Array.map method

arr = [1, 2, 3];
let testCaseIV = arr.map(plusone);
console.log(testCaseIV);

arr = [1, 2, 3];
let testCaseV = arr.map(plusI);
console.log(testCaseV);

arr = [10, 20, 30];
let testCaseVI = arr.map(constant);
console.log(testCaseVI);