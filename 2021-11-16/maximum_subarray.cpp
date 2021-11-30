class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        // create array that stores cumulative sum of `nums`;
        // cum_sum[i] = sum of nums elements up to index `i` (exclusive)
        vector<int> cum_sum;
        cum_sum.push_back(0);
        for (int i = 0; i < nums.size(); i++) {
            cum_sum.push_back(cum_sum.at(i) + nums.at(i));
        }
        
        // stores the largest subarray sum we've found
        int max_sum = nums.at(0);
        
        // store the index of the smallest value in `cum_sum`
        // that we've encountered so far
        int min_i = 0;
        
        // for each element of the cumulative sum array
        for (int i = 1; i < cum_sum.size(); i++) {
            
            // calculate the sum of `nums` elements from `min_i` (inclusive)
            // to `i` (exclusive) using the cumulative sum array
            int sum = cum_sum.at(i) - cum_sum.at(min_i);
            
            // if this is the largest sum so far, store it
            if (sum > max_sum) {
                max_sum = sum;
            }

            // if the current value in the cumulative sum array is smaller
            // than the one we stored, store the current index
            if (cum_sum.at(i) < cum_sum.at(min_i)) {
                min_i = i;
            }
        }
        return max_sum;        
    }
};
