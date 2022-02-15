class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in range(0, len(nums)):
            number = str(nums[i])
            if number in duplicates:
                return True
            else:
                duplicates[number]=True
        return False
