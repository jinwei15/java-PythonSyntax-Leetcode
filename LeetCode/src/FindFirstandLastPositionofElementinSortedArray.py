class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        resultIndex = -1
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                resultIndex = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left, right = resultIndex, resultIndex
        leftFlag, rightFlag = False, False
        while (not leftFlag or not rightFlag):
            if right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            else:
                rightFlag = True
            if left > 0 and nums[left - 1] == target:
                left -= 1
            else:
                leftFlag = True

        return [left, right]




# using binary search first find the target index

# expand the target index to the very left and right