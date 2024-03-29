/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
    var executed = false;
    var res;
    return function (...args) {
        if (!executed) {
            res = fn(...args);
            executed = true;
            return res;
        } else return undefined;
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
