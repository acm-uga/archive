class Solution {
    public int lengthOfLongestSubstring(String s) {
    int i = 0, j = 0, max = 0;
    Set<Character> set = new HashSet<>();
    
    while (j < s.length()) {
        if (!set.contains(s.charAt(i))) {
            set.add(s.charAt(i++));
            max = Math.max(max, set.size());
        } else {
            set.remove(s.charAt(j++));
            }
        }
    return max;
    }
}
