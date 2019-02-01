class HuffmanDecoder:
    def huffman(self,code_Dict,input):
        #input string
        # code_Dict string list
        if input == None or len(input) == 0:
            return None

        # read the dict into hashmap
        map = {}
        for i in range(len(code_Dict)):
            full = code_Dict[i].split()
            if full[0] == 'newline':
                map[full[1]] = '\n'
            else:
                map[full[1]] = full[0]

            print(map)
        res = []
        start = 0
        end = 1
        while(start < len(input) and end <= len(input)):
            subString = input[start:end]
            if map.get(subString):
                # substring is in the map
                res.append(map.get(subString))
                start = end
                end = start + 1
            else:
                end += 1

        return ''.join(res)

string = 'newline 1111111'
print(string.split())

a = HuffmanDecoder()
dict = ["a 100100", "b 100101", "c 110001", "d 100000", "newline 1111111", "p 111110", "q 000001"]
input = '1111100000011001001111111100101110001100000'

print(a.huffman(dict,input))
