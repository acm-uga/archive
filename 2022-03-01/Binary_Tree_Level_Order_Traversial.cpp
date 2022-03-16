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
        vector<vector<int>> v{};
        queue<TreeNode*> q{};
        q.push(root);
        while(1) {
            vector<int> b{};
            queue<TreeNode*> temp{};
            while (!q.empty()) {
                if (q.front() == nullptr) {
                    q.pop();
                    continue;
                }
                b.push_back(q.front()->val);
                temp.push(q.front()->left);
                temp.push(q.front()->right);
                q.pop();
            }
            q = temp;
            if (b.empty()) {
                break;
            } else {
                v.push_back(b);
            }
        }
        return v;
    }
};