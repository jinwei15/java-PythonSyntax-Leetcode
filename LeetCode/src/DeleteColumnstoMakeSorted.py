# The "example 1" should be explained in detail. Then at least the question would be more clear. I'll give it a go:

# Input: ["cba","daf","ghi"]
# Output: 1
# To arrive at the answer, we need to see which columns of the words aren't in non-decreasing order.
# Column 0 letters are: c, b, g. (taking the 1st letter of each string) Those letters, in that order, are non-decreasing because each letter is the same or after in the alphabet.
# Column 1 letters are: b, a, h. (taking the 2nd letter of each string) Those letters, are not in order, so we have to knock out that column.
# Column 2 letters are: a, f, i. Those letters are in order.
# So, there is only one column that breaks the requirement. Therefore only 1 column needs to be discarded. Therefore the output is 1.
# 944. Delete Columns to Make Sorted
# Easy

# 25

# 411

# Favorite

# Share
# We are given an array A of N lowercase letter strings, all of the same length.

# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

# Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

# Return the minimum possible value of D.length.

 

# Example 1:

# Input: ["cba","daf","ghi"]
# Output: 1
# Explanation: 
# After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
# If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
# Example 2:

# Input: ["a","b"]
# Output: 0
# Explanation: D = {}
# Example 3:

# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation: D = {0, 1, 2}
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for i in range(len(A[0])):
            for j in range(len(A)-1):
                if A[j][i] > A[j+1][i]:
                    ans += 1
                    break
        return ans
        
        
