class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word=""
        for ch in s:
            if ch!=" ":
                word+=ch
            else:
                if word!="":
                    words.append(word)
                    word=""
        if word !="":
            words.append(word)
        result=""
        i=len(words)-1
        while i>=0:
            result+=words[i]
            if i!=0:
                result+=" "
            i-=1
        return result
        