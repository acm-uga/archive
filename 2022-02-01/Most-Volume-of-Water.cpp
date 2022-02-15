#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int vol = 0;
        int t = 0, w = height.size() - 1;
        while (t < w) {
            bool z = (height[t] < height[w]);
            int sum = (w - t) * ((z) ? height[t] : height[w]);
            vol = max(sum, vol);
            if (z) t++;
            else w--;
        }
        return vol;
    }
};