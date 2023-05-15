/**
 * @param {Function} fn
 * @return {Function}
 */

var curry = function(fn) {
    return function curried(...args) {
        if (args.length < fn.length) {
            return function(...nextargs) {
                return curried(...args, ...nextargs);
            }
        }
        return fn(...args);
    };
};
   


function sum(a, b, c) { 
    return a + b + c; 
}

const csum = curry(sum);
console.log(csum(1,2,3));
console.log(csum(1,3)(2));
console.log(csum(1, 2)(3));