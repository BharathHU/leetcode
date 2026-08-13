class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        pw={}
        wp={}
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            p=pattern[i]
            w=words[i]
            if p in pw and pw[p] !=w:
                return False
            if w in wp and wp[w]!=p:
                return False
            pw[p]=w
            wp[w]=p
        return True
        