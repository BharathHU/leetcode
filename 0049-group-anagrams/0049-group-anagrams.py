class Solution:
    def createOccStr(self,s):
        ascii = [0] * 26
        occStr = ""
        for i in range(0, len(s)):
            ascii[ord(s[i])-97] += 1
        for i in range(0, len(ascii)):
            if ascii[i] > 0:
                occStr += chr(i + 97)
                occStr += chr(ascii[i] + 48)
        return occStr
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in range (0, len(strs)):
            occStr = self.createOccStr(strs[i])
            dict[occStr].append(strs[i])
        res = []
        for key, val in dict.items():
            res.append(val)
        return res