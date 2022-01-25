#include <vector>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        unsigned int first = 0, last = s.size() - 1;
        while (first < last) {
            swap(first++, last--, s);
        }
    }
    
    void swap(unsigned int c, unsigned int h, vector<char>& s) {
        char temp = s[h];
        s[h] = s[c];
        s[c] = temp;
    }
};