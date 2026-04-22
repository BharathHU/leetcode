class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftProd,rightProd = 1,1
        maxProd = -2**31
        i=0
        j=len(nums)-1
        while i < len(nums) and j >= 0:
            leftProd *= nums[i]
            rightProd *= nums[j]

            maxProd=max(leftProd,rightProd,maxProd)
            if leftProd == 0:
                leftProd = 1
            if rightProd == 0:
                rightProd = 1
            i += 1
            j -= 1
        return maxProd
       