class Solution {
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        ArrayList<List<Integer>> res = new ArrayList<>();
        helper(res, root, 0);
        return res;
    }
    public void helper(ArrayList<List<Integer>> res, TreeNode root, int height){
        if (root == null) return;
        
        if (res.size() <= height){
            res.add(new ArrayList<Integer>());
        }
        res.get(height).add(root.val);
        helper(res, root.left, height+1);
        helper(res, root.right, height+1);
    }
}
