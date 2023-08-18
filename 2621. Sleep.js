/**
 * @param {number} millis
 */
async function sleep(millis) {
    const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
    await sleep(millis);
    return millis;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */