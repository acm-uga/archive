class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        // problem is trivial if string length is 0 or 1
        if (s.length() <= 1) {
            return s.length();
        }
        
        // counts['a'] stores the number of 'a's we've
        // encountered so far in the string
        char counts[128] = {0};
        
        // the index of the first character in the substring
        // we are currently evaluating
        int start_i = 0;
        
        // we know a substring containing only the first character
        // in the string has no duplicate characters
        int max_length = 1;
    
        // add the first character of the string to the counts array
        counts[s[0]]++;
        
        // for each character after the first character
        for (int i = 1; i < s.size(); i++) {
            
            // if we've seen this character more than once
            if (++counts[s[i]] > 1) {
                
                // increment the substring beginning index until the duplicate
                // character is no longer in the substring; adjust counts
                // as characters are removed from the substring
                while (counts[s[i]] > 1) {
                    char substr_begin_char = s[start_i];
                    counts[substr_begin_char]--;
                    start_i++;
                }
            }
            // if the current substring, which contains no duplicate
            // characters, is longer than the longest we've found
            if (i - start_i + 1 > max_length) {
                max_length = i - start_i + 1;
            }
        }
        return max_length;
    }
};
