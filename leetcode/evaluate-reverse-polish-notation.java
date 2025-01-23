import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Set<String> opps = new HashSet<String>(Arrays.asList("+", "-", "*", "/"));
        Stack<Integer> s = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (opps.contains(tokens[i])) {
                int a = s.pop();
                int b = s.pop();
                int c = Integer.MAX_VALUE;
                if (tokens[i].equals("+")) {
                    c = a + b;
                }
                else if (tokens[i].equals("-")) {
                    c = b - a;
                }
                else if (tokens[i].equals("*")) {
                    c = a * b;
                }
                else if (tokens[i].equals("/")) {
                    c = b / a;
                }
                s.push(c);
            }
            else {
                s.push(Integer.parseInt(tokens[i]));
            }
        }
        return s.pop();
    }
}