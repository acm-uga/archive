#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int index[] = {0, 0};
        int tempIndex[] = {0, 0};
        bool shown[128]; // whole ASCII table array
        for (unsigned short t = 0; t < 128; t++) {
            shown[t] = false;
        } // for all of the shown array
        for (auto t = s.begin(); t != s.end(); t++) {
            tempIndex[1] += 1; // increment
            if (shown[*t]) { // if shown before, unmark the part of the substring with the first character
                int temp = tempIndex[0];
                while (s[temp] != *t) {
                    shown[s[temp]] = false;
                    temp++;
                } // while not the character we are looking for
                temp++; // goes over first character
                tempIndex[1] -= temp - tempIndex[0]; // get new size
                tempIndex[0] = temp; // get new place
            } else { // else see if size is max
                shown[*t] = true; // denote character is in the range now
                if (tempIndex[1] > index[1]) {
                    index[0] = tempIndex[0];
                    index[1] = tempIndex[1];
                } // if size of temp is max
            }
        }
        return index[1]; // return longest substring
    }
};