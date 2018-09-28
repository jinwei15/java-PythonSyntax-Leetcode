class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        listStr = s.split()

        # for item in listStr:
        #     item = item[::-1]
        index = 0
        while index < len(listStr):
    	# Do something to my_list[index]
            listStr[index] = listStr[index][::-1]
            index += 1

        str1 = ' '.join(listStr)

        return str1
