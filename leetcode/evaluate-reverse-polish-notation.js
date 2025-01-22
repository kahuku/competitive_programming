/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const ops = ['+', '-', '*', '/'];

    let stack = [];
    for (const token of tokens) {
        if (ops.includes(token)) {
            const b = stack.pop();
            const a = stack.pop();
            switch(token) {
                case '+':
                    stack.push(a + b);
                    break;
                case '-':
                    stack.push(a - b);
                    break;
                case '*':
                    stack.push(a * b);
                    break;
                case '/':
                    stack.push(Math.trunc(a / b));
                    break;
                default:
                    break;
            }
        }
        else {
            stack.push(parseInt(token));
        }
        // console.log(stack);
    }
    return stack[0];
};