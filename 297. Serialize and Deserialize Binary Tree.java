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
            return res
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
        return res
        
    }

// Decodes your encoded data to tree.
public TreeNode deserialize(String data) {
	String valueArray[] = data.split("X");
	TreeNode nodeArray[] = new TreeNode[valueArray.length];
	for(int i = 0; i < valueArray.length; i++) 
		if( !valueArray[i].equals("#") )
			nodeArray[i] = new TreeNode(Integer.parseInt(valueArray[i]));
	Queue<TreeNode> queue = new LinkedList<TreeNode>();
	queue.offer(nodeArray[0]);
	int size = queue.size(), index = 1;
	while( !queue.isEmpty() ) { 
		int nonNull = 0; // count the non null node of current level
		for(int i = 0; i < size; i++) { // build the tree level by level
			TreeNode peekNode = queue.poll();
			if( peekNode != null ) {
				nonNull++;
				peekNode.left = nodeArray[index];
				queue.offer(nodeArray[index++]);
				peekNode.right = nodeArray[index];
				queue.offer(nodeArray[index++]);
			}
		}
		size = nonNull * 2; // get the number of node in next level
	}
	return nodeArray[0];
}

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String data[] = data.split(",");
        TreeNode nodeArray[] = new TreeNode[valueArray.length];
        
    }
}
