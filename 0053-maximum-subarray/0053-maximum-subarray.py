class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=-2**32
        for i in range(0,len(nums)):
            currSum+=nums[i]
            if currSum >maxSum:
                maxSum=currSum
            if currSum<0:
                currSum=0
        return maxSum
