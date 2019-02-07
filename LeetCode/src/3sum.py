class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                lo = i + 1
                hi = length - 1
                sum = 0 - nums[i]
                while (lo < hi):
                    if (nums[lo] + nums[hi] == sum):
                        res.append([nums[i], nums[lo], nums[hi]])
                        while (lo < hi and nums[lo] == nums[lo + 1]): lo += 1
                        while (lo < hi and nums[hi] == nums[hi - 1]): hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < sum:
                        lo += 1
                    else:
                        hi -= 1

        return res

# The idea is to sort an input array and then run through all indices of a possible first element of a triplet. For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.

# public List<List<Integer>> threeSum(int[] num) {
#     Arrays.sort(num);
#     List<List<Integer>> res = new LinkedList<>();
#     for (int i = 0; i < num.length-2; i++) {
#         if (i == 0 || (i > 0 && num[i] != num[i-1])) {
#             int lo = i+1, hi = num.length-1, sum = 0 - num[i];
#             while (lo < hi) {
#                 if (num[lo] + num[hi] == sum) {
#                     res.add(Arrays.asList(num[i], num[lo], num[hi]));
#                     while (lo < hi && num[lo] == num[lo+1]) lo++;
#                     while (lo < hi && num[hi] == num[hi-1]) hi--;
#                     lo++; hi--;
#                 } else if (num[lo] + num[hi] < sum) lo++;
#                 else hi--;
#            }
#         }
#     }
#     return res;
# }


##TLE
# class Solution:
#     def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if nums[i]+nums[j]+nums[k] == 0 and [nums[i],nums[j],nums[k]] not in res:
#                         res.append([nums[i],nums[j],nums[k]])

#         return res