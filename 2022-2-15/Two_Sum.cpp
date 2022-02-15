#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       vector<int> ar;
        map<int, int> m;
        for(int t = 0; t < nums.size(); t++) {
            int diff = target - nums[t];
            if(m.count(diff)) {
                ar.push_back(m.find(diff)->second);
                ar.push_back(t);
            } else {
                m.insert({nums[t],t});
            }
        }
        return ar;
    }
};