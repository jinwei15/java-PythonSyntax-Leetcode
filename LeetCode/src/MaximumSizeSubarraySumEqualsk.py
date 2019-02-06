# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:

# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        ans, acc = 0, 0               # answer and the accumulative value of nums
        mp = {0:-1}                 #key is acc value, and value is the index
        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i 
            if acc-k in mp:
                ans = max(ans, i-mp[acc-k])
        return ans
        
        
# public int maxSubArrayLen(int[] nums, int k) {
#     int sum = 0, max = 0;
#     HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
#     for (int i = 0; i < nums.length; i++) {
#         sum = sum + nums[i];
#         if (sum == k) max = i + 1;
#         else if (map.containsKey(sum - k)) max = Math.max(max, i - map.get(sum - k));
#         if (!map.containsKey(sum)) map.put(sum, i);
#     }
#     return max;
# }
