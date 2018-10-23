class Bubble:
    def BubbleSort(self,badList):
        A = badList.copy()
        lengthA = len(A)
        for i in range(lengthA):
            flag = False
            for j in range(0,lengthA-2-i):
                if A[i] > A[i+1]:
                    temp = A[i]
                    A[i] = A[i+1]
                    A[i+1] = temp
                    flag = True
            if flag == False:
                break
        return A

array = [2,7,4,1,5,3]

p1 = Bubble()

print(p1.BubbleSort(array))


