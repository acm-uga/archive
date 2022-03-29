#include <vector>

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> v{};
        if (root != nullptr) inorder(v,root);
        return v;
    }
    
    void inorder(vector<int> &v, TreeNode* r) {
        if (r->left != nullptr) inorder(v, r->left);
        v.push_back(r->val);
        if (r->right != nullptr) inorder(v, r->right);
    }
};