#include <vector>
#include <queue>
using namespace std;

 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> v{}; // returns
        queue<TreeNode*> q{}; // level of tree
        q.push(root); // level 0
        while(1) { // inf
            vector<int> b{}; // container for values
            queue<TreeNode*> temp{}; // next level
            while (!q.empty()) {
                if (q.front() == nullptr) {
                    q.pop();
                    continue;
                } // if child is null, pop it and continue
                b.push_back(q.front()->val); // puts values
                temp.push(q.front()->left);
                temp.push(q.front()->right); // gets children
                q.pop(); // pop front
            } // while the level is not done
            q = temp; // switch to next level
            if (b.empty()) {
                break;
            } else {
                v.push_back(b);
            } // if no more children, break, else push level values
        } // while infinite
        return v; // return values
    } // levelOrder
};