#include <string>

using namespace std;

class Solution {
public:
    string interpret(string command) {
        int t = 0;
        string str = "";
        while (t < command.size()) {
            if (command[t] == 'G') {
                str += 'G';
                t++;
                continue;
            } else if (command[t] == '(' && command[t + 1] == ')') {
                str += 'o';
                t += 2;
                continue;
            }
            str += "al";
            t += 4;
        }
        return str;
    }
};