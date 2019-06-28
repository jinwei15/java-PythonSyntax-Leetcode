"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file 真心没弄懂
"""


class Solution:
    #     def read(self, buf, n):
    #         """
    #         :type buf: Destination buffer (List[str])
    #         :type n: Number of characters to read (int)
    #         :rtype: The number of actual characters read (int)
    #         """
    #         eof = False
    #         total = 0
    #         tmp = [None,None,None,None]

    #         while not eof and total < n:
    #             count = read4(tmp)
    #             # check if it's the end of the file
    #             eof = count < 4
    #             # get the actual count
    #             count = min(count, n - total)
    #             # copy from temp buffer to buf
    #             for i in range(count):
    #                 total+=1
    #                 buf[total] = tmp[i];
    #         return total

    def read(self, buf, n):
        idx = 0
        while n > 0:
            # read file to buf4
            buf4 = [""] * 4
            l = read4(buf4)
            # if no more char in file, return
            if not l:
                return idx
            print(buf4)
            print(l)
            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx

# public int read(char[] buf, int n) {
#   boolean eof = false;      // end of file flag
#   int total = 0;            // total bytes have read
#   char[] tmp = new char[4]; // temp buffer
#   while (!eof && total < n) {
#     int count = read4(tmp);
#     // check if it's the end of the file
#     eof = count < 4;
#     // get the actual count
#     count = Math.min(count, n - total);
#     // copy from temp buffer to buf
#     for (int i = 0; i < count; i++)
#       buf[total++] = tmp[i];
#   }
#   return total;
# }