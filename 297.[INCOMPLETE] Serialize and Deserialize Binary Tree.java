/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        string res = "";
        if (root == null) {
            return res;
        }
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root)
        while (!queue.isempty()) {
            TreeNode node = queue.poll();
                res += node.val.toString() + ",";
                if (node.left != null) {
                    queue.offer(node.left);
                } else {
                    res += "#,";
                }
                if (node.right  != null) {
                    queue.offer(node.right);
                } else {
                    res += "#,";
                }
        }
        return res;
        
    }
	// Decodes your encoded data to tree.
    public TreeNode deserialize(String data) { // DFS
        String data[] = data.split(",");
        TreeNode nodeArray[] = new TreeNode[valueArray.length];
        
    }
}
