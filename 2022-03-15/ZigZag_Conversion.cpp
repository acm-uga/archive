#include <string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        string str = "";
        if (numRows == 1) return s;
        int amount = 2 *numRows - 2;
        for (int t = 0; t < numRows; t++) {
            for (int i = 0; i + t < s.size(); i += amount) {
                char c = s[i + t];
                str += c;
                if (t != 0 && t != numRows - 1 && i + amount - t < s.size()) {
                    c = s[(i + amount - t)];
                    str += c;
                }
            }
        }
        return str;
    }
};