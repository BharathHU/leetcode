class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

        for i in range(len(s)):
            if "A" <= s[i] <= "Z":
                newstr += chr(ord(s[i]) + 32)
            elif ("0" <= s[i] <= "9") or ("a" <= s[i] <= "z"):
                newstr += s[i]

        # check palindrome
        left, right = 0, len(newstr) - 1
        while left < right:
            if newstr[left] != newstr[right]:
                return False
            left += 1
            right -= 1

        return True