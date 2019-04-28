class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1

        #find the pivot
        pivot = 0
        left = 0
        right = len(nums)-1 #

        while(left<right):
            mid = (left+right)//2
            # if nums[mid] == target:
            #     return mid
            if nums[mid] > nums[right]:
                    left = mid + 1
            else:
                    right = mid

        pivot = right
        print(pivot)
        left = 0
        right = len(nums)-1 #
        if target <= nums[right]:
            left = pivot
        else:
            right = pivot

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1
