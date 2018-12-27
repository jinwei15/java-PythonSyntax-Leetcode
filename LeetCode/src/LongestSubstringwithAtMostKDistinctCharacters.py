class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """


       # Initialize sliding window and counts of chars in the window
        # Worst case time and space complexity:
        # Time: O(N), Space: O(W) where N is size of string and W is size of max window
        
        left = 0
        right = 0
        counts = dict()
        maxlength = 0
        # Slide the window down the string until we reach the end
        #
        # Loop invariant:
        # (1) The previously seen window is s[left:right]
        # (2) The right index - left index of window is always the length
        #     of the longest substring with <= 2 distinct characters
        while right < len(s):
            # Slide the right end up and update counts such that the window is now s[left:right+1]
            counts[s[right]] = counts.get(s[right],0) + 1
            right += 1
            
            # If the window has more than 2 characters, slide the left end of 
            # the window up and update counts such that the window is now s[left+1:right+1]
            if len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            # print(right - left, " sep", left, right)
        # The length of the window is the length of the longest valid substring
        return right - left
        
