class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastNum = {}
        for i in range(0, len(nums)):
            currentNum = nums[i]
            if target-currentNum in pastNum:
                return [i, pastNum[target-currentNum]]
            else:
                pastNum[currentNum]=i