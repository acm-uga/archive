class Solution {
    public int maxArea(int[] height) {
        int res = 0;
        int start = 0;
        int end = height.length -1;
        int step = 0;
        while(start < end){
            step = (Math.min(height[start], height[end])) * (end - start);
            if (height[start] > height[end]) end--;
            else start++;
            res = Math.max(res, step);
        }
        return res;
    }
} 
