class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if matrix == [] or len(matrix[0]) == 0:
            return False
        row_num = len(matrix)
        col_num = len(matrix[0])
        begin = 0
        end = row_num * col_num - 1
        while begin <= end:
            mid = (begin + end) // 2
            mid_value = matrix[mid // col_num][mid % col_num]

            if (mid_value == target):
                return True

            elif (mid_value < target):
                # Should move a bit further, otherwise dead loop.
                begin = mid + 1
            else:
                end = mid - 1
        return False
        # for row in matrix:
        #     if target in row:
        #         return True
        # return False

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
