class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        res=[]
        for num in nums2:
            if num in s1:
                res.append(num)
                s1.remove(num)
        return res


        