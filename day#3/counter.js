var createCounter = function (init) {
    let n = init
    var increment = function () {
        return n = n + 1;
    }
    var decrement = function () {
        return n = n - 1;
    }
    var reset = function () {
        n = init;
        return n;
    }
    return { increment, reset, decrement }
};


const testCase1 = createCounter(5)
console.log(testCase1.increment());
console.log(testCase1.reset());
console.log(testCase1.decrement());


const testCase2 = createCounter(0)
console.log(testCase2.increment());
console.log(testCase2.increment());
console.log(testCase2.decrement());
console.log(testCase2.reset());
console.log(testCase2.reset());