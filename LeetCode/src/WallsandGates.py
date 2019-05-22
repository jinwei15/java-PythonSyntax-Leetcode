class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        empty = 2 ** 31 - 1
        q = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0: q.append((i, j, 0))

        r, c = len(rooms), len(rooms[0])

        while q:
            x, y, val = q.popleft()
            if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] < val:
                continue
            rooms[x][y] = val
            q.extend([(x + 1, y, val + 1), (x - 1, y, val + 1), (x, y + 1, val + 1), (x, y - 1, val + 1)])


