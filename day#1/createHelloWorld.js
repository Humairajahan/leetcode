let createHelloWorld = function () {
    return function (...args) {
        return "Hello World"
    }
};


const f = createHelloWorld();
const output = f();
console.log(output);