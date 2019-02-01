class NoPairsAllowed:
    def minimalOperations(self, input):
        #input is string array
        inputLength = len(input)
        res = [0 for _ in range(inputLength)]
        for i in range(inputLength):
            start = 0
            end = 1
            while(len(input[i]) >= 2 and  end < len(input[i])):
                if input[i][start] != input[i][end]:

                    diff = end - start
                    res[i] += diff // 2
                    start = end
                    end = start + 1
                else:
                    end += 1

            if end - start >= 2:
                res[i] += (end - start)//2

        return res

a = NoPairsAllowed()
input1 = ["ab", "aab", "abb", "abab", "abaaaba"]
print(a.minimalOperations(input1))

input2= ["add", "boook", "break"]
print(a.minimalOperations(input2))
