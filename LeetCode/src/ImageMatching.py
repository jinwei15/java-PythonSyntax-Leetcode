import collections


class ImageMatching:
    def ImageMatching(self, map1, map2):
        match = 0
        for i in range (len(map1)):
            for j in range(len(map1[i])):
                record1 = self.bfs(map1,i,j)
                record2 = self.bfs(map2,i,j)

                if (self.isMatch(record1,record2)):
                    match += 1

        return  match


    def isMatch(self,record1,record2):

        if len(record1) != len(record2):
            return  False
        if len(record1) == 0:
            return False

        for i in range(len(record1)):
            if record1[i][0] != record2[i][0] or record1[i][1] != record2[i][1]:
                return False
        return True


    def bfs(self, map, row, col):
        res = []
        if map[row][col] == 1:
            queue = collections.deque()
            queue.append([row, col])
            while len(queue) > 0:
                temp = queue.popleft()
                r = temp[0]
                c = temp[1]
                map[r][c] = 0
                res.append(temp)

                #check four directions
                if (r - 1 >= 0 and c < len(map[r - 1]) and map[r - 1][c] == 1):
                    queue.append([r-1,c])
                if (r + 1 < len(map) and c < len(map[r + 1]) and map[r + 1][c] == 1) :
                    queue.append([r+1, c])
                if (c - 1 >= 0 and map[r][c - 1] == 1):
                    queue.append([r,c-1])
                if (c + 1 < len(map[r]) and map[r][c + 1] == 1) :
                    queue.append([r, c+1])


        return res



map1a = []
map1a.append([0,0,1])
map1a.append([0,1,1])
map1a.append([1,0,1])

map1b  = []
map1b.append([0,0,1])
map1b.append([0,1,1])
map1b.append([0,0,1])


res = ImageMatching().ImageMatching(map1a,map1b)
print(res)



