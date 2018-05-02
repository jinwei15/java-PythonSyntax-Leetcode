/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class MaximumDepthofBinaryTree {

	/**
	 * @param args
	 *            Given a binary tree, find its maximum depth.
	 * 
	 *            The maximum depth is the number of nodes along the longest path
	 *            from the root node down to the farthest leaf node.
	 * 
	 *            Note: A leaf is a node with no children.
	 * 
	 *            Example:
	 * 
	 *            Given binary tree [3,9,20,null,null,15,7],
	 * 
	 *            3 / \ 9 20 / \ 15 7 return its depth = 3.
	 * 
	 * 
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class MaximumDepthofBinaryTreeSolution {
	public int maxDepth(TreeNode root) {
		return theMax(root, 1);
	}

	public int theMax(TreeNode root, int i) {
		if (root == null)
			return 0;
		if (root.left != null || root.right != null) {

		}
		return i;

	}
}
