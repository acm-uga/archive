#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> m{};
        for (auto t = nums.begin(); t != nums.end(); t++) {
            if (m.count(*t) == 0) {
                m[*t] = 1;
            } else {
                return true;
            }
        }
        return false;
    }
};