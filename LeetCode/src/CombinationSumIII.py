class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(list(range(1, 10)), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and sum(path) == n:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n, i + 1, path + [nums[i]], res)

