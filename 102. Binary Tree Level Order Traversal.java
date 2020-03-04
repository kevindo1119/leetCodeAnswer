/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        
        if (root == null) {
            return res;
        }
        
        // 1. 创建一个队列，把起始节点都放进去
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        // 2. while 队列不空，处理队列中的节点，并拓展出新的节点
        while (!queue.isEmpty()) {
            // for 上一层的节点拓展下一层的节点
            // queue.size() 写在for loop 里面的问题是， queue.size是改变的，不能完成层拓展，但是也没有问题。
            List<Integer> level = new ArrayList<>();
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right  != null) {
                    queue.offer(node.right);
                }
            }
            res.add(level);
        }
        
        return res;
    }
}
