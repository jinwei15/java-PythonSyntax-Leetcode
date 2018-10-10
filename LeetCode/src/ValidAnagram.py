class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()
        for ch in s:
            s_dict[ch] =  s_dict.get(ch,0) + 1
        for ch in t:
            t_dict[ch] =  t_dict.get(ch,0) + 1

        for key in s_dict:
            if key not in t_dict or t_dict[key] != s_dict[key]:
                return False


        return True


        """
        in java or python it can be done by sending all the characters in an array/List
        and sorted . then check if they are equal.

        public boolean isAnagram(String s, String t) {
            if (s.length() != t.length()) {
                return false;
            }
            char[] str1 = s.toCharArray();
            char[] str2 = t.toCharArray();
            Arrays.sort(str1);
            Arrays.sort(str2);
            return Arrays.equals(str1, str2);
        }


        """
