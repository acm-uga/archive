/**
 * Leetcode Problem: https://leetcode.com/problems/valid-parentheses/
 */
class Solution {
public:
    
    bool isValid(string s) {
        
        // convert string to doubly linked-list to allow O(1) deletion
        list<char> s_copy {s.begin(), s.end()};
        
        // iterate over each element except the last or until list size is 0
        for (auto s_iter {s_copy.begin()}; s_copy.size() > 1 && s_iter != prev(s_copy.end());) {
            
            // due to ascii proximity and char restrictions in `s`,
            // this will detect: [] or {} or ()
            if (*s_iter - *(next(s_iter)) == -1 || *s_iter - *(next(s_iter)) == -2) {
                
                // delete a pair if a valid one is found
                s_copy.erase(s_iter++);
                s_copy.erase(s_iter++);
                
                // if we are not at the beginning of the list, go back one character
                if (s_iter != s_copy.begin()) {
                    s_iter--;
                }
                
            // if a pair of parentheses or braces was not found, move forward in the list
            } else {
                s_iter++;
            }
        }

        // if the entire string was deleted, it must've been valid
        return s_copy.size() == 0;
    }
};
