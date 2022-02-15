#include <vector>
#include <limits.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = INT_MAX;
        int maxp = 0;
        for (auto t = prices.begin(); t != prices.end(); t++) {
            if (min > *t) {
                min = *t;
                continue;
            }
            maxp = max(maxp, *t - min);
        }
        return maxp;
    }
};