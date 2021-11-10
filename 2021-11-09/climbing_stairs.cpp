/**
 * https://leetcode.com/problems/climbing-stairs/
 * 
 * Solution works by using the fact that the number of ways to climb N steps
 * is equal to `number of ways to climb N - 1 steps` + `number of ways to climb
 * N - 2 steps`; the two possibilities for climbing N steps are climb N - 1
 * steps and then climb 1 step or climb N - 2 steps then climb 1 step.
 */

class Solution {
public:
    int climbStairs(int n) {
        
        int prev = 0;
        int curr = 1;
        
        while (n > 0) {
            curr += prev;
            prev = curr - prev;
            n--;
        }
        
        return curr;
    }
};
