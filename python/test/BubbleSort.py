class Bubble:
    def BubbleSort(self,A):
        lengthA = len(A)
        for i in range(lengthA):
            flag = False
            for j in range(0,lengthA-2-i):
                if A[j] > A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp
                    flag = True
            if flag == False:
                break
        return A

array = [2,7,4,1,5,3]

b = Bubble()

print(b.BubbleSort(array))


