/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    p = 0;
    m = prices[0];
    for (price of prices) {
        m = Math.min(price, m);
        p = Math.max(p, price - m);
    }
    return p;
};