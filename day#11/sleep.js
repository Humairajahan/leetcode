/**
 * @param {number} millis
 */

function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

let t = Date.now()
sleep(2000).then(() => console.log(Date.now() - t))