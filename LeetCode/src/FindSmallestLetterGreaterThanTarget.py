class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while (left < right):
            mid = (left + right) >> 1
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[(left) % len(letters)]
        # if left <len(letters) and letters[left]==target:
        #     return letters[(left+1)%len(letters)]
        # else :
        #     return letters[(left)%len(letters)]

# ["e","e","e","e","e","e","n","n","n","n"]
# "e"

# should return n


# a bit same to 35 find insert position
