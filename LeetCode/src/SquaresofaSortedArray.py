# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         return sorted([i**2 for i in A])


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        i, j = 0, n - 1
        result = [None for _ in range(n)]
        for p in range(n - 1, -1, -1):
            if abs(A[i]) > abs(A[j]):
                result[p] = A[i] * A[i]
                i += 1
            else:
                result[p] = A[j] * A[j]
                j -= 1
        return result

# class Solution {
#     public int[] sortedSquares(int[] A) {
#         int n = A.length;
#         int[] result = new int[n];
#         int i = 0, j = n - 1;
#         for (int p = n - 1; p >= 0; p--) {
#             if (Math.abs(A[i]) > Math.abs(A[j])) {
#                 result[p] = A[i] * A[i];
#                 i++;
#             } else {
#                 result[p] = A[j] * A[j];
#                 j--;
#             }
#         }
#         return result;
#     }
# }