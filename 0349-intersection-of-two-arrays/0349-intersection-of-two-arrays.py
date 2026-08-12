class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        res=[]
        for num in nums1:
            freq[num]=1
        for num in nums2:
            if num in freq:
                if num not in res:
                    res.append(num)
        return res


        