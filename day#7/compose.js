/**
 * @param {Function[]} functions
 * @return {Function}
 */

var compose = function (functions) {
    if (functions.length == 0) {
        return function (x) {
            return x;
        };
    }
    else {
        return function (x) {
            final_val = x;
            for (let index = functions.length - 1; index >= 0; index--) {
                final_val = functions[index](final_val);
            }
            return final_val;
        }
    }
};


let testCaseI = compose([x => x + 1, x => 2 * x]);
console.log(testCaseI(4));

let testCaseII = compose([x => 10 * x, x => 10 * x, x => 10 * x]);
console.log(testCaseII(1));

let testCaseIII = compose([]);
console.log(testCaseIII(42));
