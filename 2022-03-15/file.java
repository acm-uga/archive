class Solution {
    public String interpret(String command) {
        String goal = "";
        int start = 0;
        int end = 2;
        
        while (end <= command.length() + 1 ) {
            if (command.charAt(start) == 'G') {
                goal += "G";
                start++;
                end++;
            } else if (command.substring(start, end).equals("(a")) {
                goal += "al";
                start += 4;
                end += 4;
            } else if (command.substring(start, end).equals("()")) {
                goal += "o";
                start += 2;
                end += 2;
            } else {
                start++;
                end++;
            }
        } // while
        
        return goal;
    } // interpret
}
