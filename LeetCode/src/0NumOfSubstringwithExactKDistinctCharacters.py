class Solution:

# slicing windows
    def findSubstring(self, str, k):
        if str is None or len(str) == 0:
            return 0

        ch_count = {}

        n = len(str)
        start, end = 0, 0

        count = 0
        while end < n:

            ch_count[str[end]] = ch_count.get(str[end], 0) + 1

            if len(ch_count) == k:
                count += self.getCount(end, str, ch_count)
                ch_count[str[start]] -= 1
                if ch_count[str[start]] == 0:
                    del ch_count[str[start]]
                start += 1

            if len(ch_count) < k:
                end += 1

        return count

    def getCount(self, end, str, ch_count):
        n = len(str)
        count = 0
        while end < n:
            if str[end] not in ch_count:
                break
            count += 1
            end += 1

        return count


# two for loop. with a break there is no difference with slicing windows
class Solution2:
    def findSubstring(self, str, k):
        if str is None or len(str) == 0:
            return 0

        checkTable = dict()
        resultNum = 0
        for i in range(len(str)):
            checkTable.clear()
            for j in range(i, len(str)):
                checkTable[str[j]] = checkTable.get(str[j], 0) + 1
                if len(checkTable) == k:
                    resultNum += 1
                    print(checkTable)
                elif len(checkTable) > k:
                    break
        return resultNum








bb = Solution2()
result = bb.findSubstring("eeecbdf", 3)
print(result)
