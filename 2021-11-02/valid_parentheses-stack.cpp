#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st{}; // works on last-in, first-out principle (LiFo or FiLo)
        for (auto t = s.begin(); t != s.end(); t++) {
            switch (*t) {
                case '{':
                case '[':
                case '(': // open bracket
                    st.push(*t); // pushes the character to the top of the stack
                    break; // breaks switch
                case ')':
                case ']':
                case '}': // close bracket
                    if (st.empty() || getOther(st.top()) != *t) {
                        return false;
                    } // if stack is empty or if the top of the stack does not correspond to the specific closed bracket
                    st.pop(); // takes the open bracket off the stack
                    break; // breaks switch
                default: // values we do not have to worry about
                    continue;
            } // switch for every possible value
        } // for every character in the string
        return st.empty(); // returns if the stack is empty or not
    }
    
    char getOther(char c) {
        switch (c) {
                case '{':
                    c = '}';
                    break;
                case '[':
                    c = ']';
                    break;
                case '(':
                    c = ')';
                    break;
                case ')':
                    c = '(';
                    break;
                case ']':
                    c = '[';
                    break;
                case '}':
                    c = '{';
                    break;
                default:
                    c = c;
            } // switch
        return c;
    } // gets the corresponding bracket
};