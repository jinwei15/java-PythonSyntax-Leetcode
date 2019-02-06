# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':

        result = []
        if root == None: return result
        queue = collections.deque()
        queue.append([root])
        result.append([root.val])
        while len(queue) != 0:
            temp = []
            tempTree = []
            curr = queue.popleft()
            for i in curr:
                if i.left != None:
                    temp.append(i.left.val)
                    tempTree.append(i.left)
                if i.right != None:
                    temp.append(i.right.val)
                    tempTree.append(i.right)
            if temp:
                queue.append(tempTree)
                result.append(temp)
        return result
                
                
            
# public class Solution {
#     public List<List<Integer>> levelOrder(TreeNode root) {
#         Queue<TreeNode> queue = new LinkedList<TreeNode>();
#         List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
        
#         if(root == null) return wrapList;
        
#         queue.offer(root);
#         while(!queue.isEmpty()){
#             int levelNum = queue.size();
#             List<Integer> subList = new LinkedList<Integer>();
#             for(int i=0; i<levelNum; i++) {
#                 if(queue.peek().left != null) queue.offer(queue.peek().left);
#                 if(queue.peek().right != null) queue.offer(queue.peek().right);
#                 subList.add(queue.poll().val);
#             }
#             wrapList.add(subList);
#         }
#         return wrapList;
#     }
# }
