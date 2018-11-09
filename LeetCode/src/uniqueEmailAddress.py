class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        mailList = set()
        for addr in emails:
            allIn = addr.split('@')
            allIn[0] = allIn[0][:allIn[0].index('+')]
            allIn[0] = allIn[0].replace('.','')
            mailList.add(allIn[0] +'@'+allIn[1])
        # print(mailList)
        return len(mailList)
