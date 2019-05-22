# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         for i in range(len(T)):
#             day = 0
#             for j in range(i+1,len(T)):
#                 day += 1
#                 if T[j] > T[i]:
#                     break
#                 if T[j] <= T[i] and j == len(T) -1:
#                     day = 0
#                     break
#             T[i] = day
#         return T

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T)-1,-1,-1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                # print(i,' ',stack)
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans