# dfs solutions
class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':
        row = len(image)
        col = len(image[0])
        origin = image[sr][sc]
        if origin == newColor:
            return image

        def dfs(image, r, c, newColor):
            curr = image[r][c]
            if curr != origin:
                return

            image[r][c] = newColor

            if r - 1 >= 0 and image[r - 1][c] == curr:
                dfs(image, r - 1, c, newColor)
            if r + 1 < row and image[r + 1][c] == curr:
                dfs(image, r + 1, c, newColor)
            if c - 1 >= 0 and image[r][c - 1] == curr:
                dfs(image, r, c - 1, newColor)
            if c + 1 < col and image[r][c + 1] == curr:
                dfs(image, r, c + 1, newColor)

        dfs(image, sr, sc, newColor)
        return image

# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]

# sr = 1
# sc = 1
# newColor = 2
# print(Solution().floodFill(image,sr,sc,newColor))

# bfs solutions
# class Solution:
#     def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':
#         """
#         111
#         110
#         101
#         click on the (1,1) and becomes

#         222
#         220
#         201
#         """
#         if len(image) == 0 or len(image[0])==0 or image == None or image[sr][sc] == newColor:
#             return image

#         q = collections.deque()
#         q.append((image[sr][sc], Point(sr,sc)))
#         row,col = len(image),len(image[0])

#         while(len(q)!=0):
#             (curr, pointNow)= q.popleft()
#             currX = pointNow.x
#             currY = pointNow.y
#             image[currX][currY] = newColor
#             if currX - 1 >= 0 and image[currX-1][currY] == curr:
#                 q.append((image[currX - 1][currY], Point(currX - 1,currY)))
#             if currX + 1 < row and image[currX+1][currY] == curr:
#                 q.append((image[currX + 1][currY], Point(currX + 1,currY)))
#             if currY - 1 >= 0 and image[currX][currY-1] == curr:
#                 q.append((image[currX][currY-1], Point(currX ,currY-1)))
#             if currY + 1 < col and image[currX][currY+1] == curr:
#                 q.append((image[currX][currY+1], Point(currX,currY+1)))
#         return image

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y




