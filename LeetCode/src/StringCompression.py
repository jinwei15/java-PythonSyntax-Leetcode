class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 0
        indexAns = 0
        while(index < len(chars)):
            currChar = chars[index]
            count = 0
            while(index < len(chars) and chars[index] ==currChar):
                index += 1
                count += 1
            # indexAns += 1
            # chars[indexAns] = currentChar
            print(index,count,'for',chars[index-1])
            chars[indexAns] = currChar
            indexAns += 1
            
            if count != 1:
                for i in str(count):
                    chars[indexAns] = i
                    indexAns += 1
        return indexAns
                
    # public int compress(char[] chars) {
    #     int indexAns = 0, index = 0;
    #     while(index < chars.length){
    #         char currentChar = chars[index];
    #         int count = 0;
    #         while(index < chars.length && chars[index] == currentChar){
    #             index++;
    #             count++;
    #         }
    #         chars[indexAns++] = currentChar;
    #         if(count != 1)
    #             for(char c : Integer.toString(count).toCharArray()) 
    #                 chars[indexAns++] = c;
    #     }
    #     return indexAns;
    # }
