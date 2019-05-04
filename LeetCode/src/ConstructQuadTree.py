
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: 'List[List[int]]') -> 'Node':


        if len(grid) == 0: return None
        
        flag = grid[0][0]
        for item in grid:
            if not all(p == flag for p in item):
                flag = -1
                break
  
        if flag != -1: return Node(flag,True,flag,flag,flag,flag)

        
        row,col = len(grid) ,len(grid[0]) 
        
        root = Node(False,False,None,None,None,None)
        root.topLeft = self.construct([l[0:col//2] for l in grid[0:row//2]])

        root.topRight = self.construct([l[col//2:col] for l in grid[0:row // 2]])
        root.bottomLeft = self.construct( [l[0:col//2] for l in grid[row//2:row]])
        root.bottomRight = self.construct( [l[col//2:col] for l in grid[row//2:row]])
        
        
        return root


if __name__ == "__main__":
    print("start fo the program")
    case = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]

    bb = Solution()
    print(bb.construct(case))


