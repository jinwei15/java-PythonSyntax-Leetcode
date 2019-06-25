# write a method to replace all space in a string

# input 'Mr John Smith    ', 13
# output 'Mr%20John%20Smith'

class Solution:
    def URLify(self, string, number):
        print(string)
        print(number)
        ret = string.rstrip()
        ret.replace(' ','%20')


        return ret.replace(' ','%20')

    # if __name__== "__main__":
    #     # URLify('Mr John Smith    ', 5)


a = Solution()

print(a.URLify('Mr John Smith    ',5))