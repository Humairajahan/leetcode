var createCounter = function (n) {
    let init = n - 1;
    return function () {
        return init = init + 1;
    };
};

const counter = createCounter(10)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12
