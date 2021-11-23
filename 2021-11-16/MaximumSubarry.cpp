#include <vector>

#define max(A,B) ((A) > (B)) ? A : B
#define INT32_MIN -2147483648

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int man = 0, temp = 0, mix = INT32_MIN; // man is max, temp is temporary max, mix is min
        for (auto t = nums.begin(); t != nums.end(); t++) {
            temp += *t; // add current number
            mix = max(*t, mix); // mix becomes maximum value of vector
            if (temp < 0) {
                temp = 0;
                continue;
            }  // if having the other values is more trouble than it's worth
            if (temp > man) {
                man = temp;
            } // if temp is the new max sum
        } // for all of the vector
        return (man == 0) ? mix : man; // if man is the minimum value it can be
    }
};