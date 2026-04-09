class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict={}
        dupli=[]
        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for key,val in dict.items():
            if val>1:
                dupli.append(key)
        return dupli
        