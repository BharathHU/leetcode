class Solution:
    def fourSumCount(self, num1: List[int], num2: List[int], num3: List[int], num4: List[int]) -> int:
        count=Counter()
        for a in num1:
            for b in num2:
                count[a+b]+=1
        ans=0
        for c in num3:
            for d in num4:
                ans+=count[-(c+d)]
        return ans

        