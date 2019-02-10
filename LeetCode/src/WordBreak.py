class Solution(object):
    def wordBreak(self, s, wordDict):
        # """
        # :type s: str
        # :type wordDict: List[str]
        # :rtype: bool
        # """
        ############## DP###################
        # wordDictSet = set(wordDict)
        # dp = [False for _ in range(len(s)+1)]
        # dp[0] = True
        # for i in range(1,len(s)+1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordDictSet:
        #             dp[i] = True
        #             break
        # return dp[len(s)]
        ############## recursion #############

        def recursion(s, setDict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in setDict and recursion(s, setDict, end):
                    return True
            return False

        return recursion(s, set(wordDict), 0)

# DP solving
# public class Solution {
#     public boolean wordBreak(String s, List<String> wordDict) {
#         Set<String> wordDictSet=new HashSet(wordDict);
#         boolean[] dp = new boolean[s.length() + 1];
#         dp[0] = true;
#         for (int i = 1; i <= s.length(); i++) {
#             for (int j = 0; j < i; j++) {
#                 if (dp[j] && wordDictSet.contains(s.substring(j, i))) {
#                     dp[i] = true;
#                     break;
#                 }
#             }
#         }
#         return dp[s.length()];
#     }
# }


#  use recursion and backtracking.
# public class Solution {
#     public boolean wordBreak(String s, List<String> wordDict) {
#         return word_Break(s, new HashSet(wordDict), 0);
#     }
#     public boolean word_Break(String s, Set<String> wordDict, int start) {
#         if (start == s.length()) {
#             return true;
#         }
#         for (int end = start + 1; end <= s.length(); end++) {
#             if (wordDict.contains(s.substring(start, end)) && word_Break(s, wordDict, end)) {
#                 return true;
#             }
#         }
#         return false;
#     }
# }