/**
 * @param {Function} fn
 */

function memoize(fn) {
    results = {};
    return function(...args) {
        if (args in results) {
            return results[args];
        }
        else {
            fn_val = fn(...args);
            results[args] = fn_val;
            return fn_val;
        }
    }
}

let callCount;

let sum = function (a,b) {
    callCount++;
    return a + b;
}

// let factorial = function (n) {
//     if (n <= 1) {
//         return 1;
//     }
//     else {
//         return factorial(n-1) * n;
//     }
// }

// let fib = function (n) {
//     if (n <= 1) {
//         return 1;
//     }
//     else if (n == 2) {
//         return 2;
//     }
//     else {
//         return fib(n-1) + fib(n-2);
//     }
// }

callCount = 0;
let testCaseI = memoize(sum);
console.log(testCaseI(2, 3)); // 5
console.log(testCaseI(2, 3)); // 5
console.log(callCount); // 1 
