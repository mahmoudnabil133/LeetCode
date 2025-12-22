1/**
2 * @param {number} millis
3 * @return {Promise}
4 */
5async function sleep(millis) {
6    return new Promise(res=> setTimeout(res, millis))
7}
8
9/** 
10 * let t = Date.now()
11 * sleep(100).then(() => console.log(Date.now() - t)) // 100
12 */