class Solution:
    def longestPalindrome(self, s):
        if not s:
            return s
        longest_palindrome_sub = ""
        for i in range(len(s)):
            j = i+1
            while len(s[i:]) > len(longest_palindrome_sub) and j <= len(s):
                if s[i:j]==s[i:j][::-1] and len(longest_palindrome_sub)< len(s[i:j]):
                    longest_palindrome_sub = s[i:j]
                j = j+1

        return longest_palindrome_sub

s= Solution()
print(s.longestPalindrome("babad"))



