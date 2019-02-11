#
#
# 1. Count number of substrings with exactly k distinct characters
#
# ..给一个字符串，求满足条件的substring的数量：substring有刚好K个distinct characters
# https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/
#
# ..最多含k个字母的substr
#
# ..k distinct character：我就直接用的hashset存字符的O(n^2)解法，
# 可以过test case，但是需要注意的是，如果k=0，需要返回0，我当时一直以为空字符串也属于答案，返回1。。被这个case卡了40分钟。。
#
# ..利口散司令 找所有的substring最多重复k个character
#
# ..substring with k distinct characters 给字符串和k，找子串，子串里面的不同的字母有k个，问有多少这样的子串
#
# ..the number of the substring with exactly k distinct character.
# 我用的two for loop with hashmap. 因为写完时间还有太多，我又试了试用two pointer，但是好像并不行，但是我最后也并没有搞懂为什么two pointer不行。查了查好像最优的就是O(n2)。不知道地里大神有没有高见。我总是觉得好像能搞一个O(n)的出来。
#
# ..coding一道是k distinct substring, 类似蠡口159, 但千万注意返回是一共有多少这样的子串，而不是找其中最长的一个
#
# ..geekforgeeks..https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/

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


