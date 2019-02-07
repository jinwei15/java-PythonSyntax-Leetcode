class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        for row in matrix:
            if target in row:
                return True
        return False

# class Solution {
#     public:
#         bool searchMatrix(vector<vector<int> > &matrix, int target) {
#             int n = matrix.size();
#             int m = matrix[0].size();
#             int l = 0, r = m * n - 1;
#             while (l != r){
#                 int mid = (l + r - 1) >> 1;
#                 if (matrix[mid / m][mid % m] < target)
#                     l = mid + 1;
#                 else
#                     r = mid;
#             }
#             return matrix[r / m][r % m] == target;
#         }
# };