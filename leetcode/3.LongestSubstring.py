class Solution:
    def lengthOfLongestSubstring(self, s):
        mylist = []
        max_length = 0
        for i in range(len(s)):
            c = s[i]
            if c not in mylist:
                mylist.append(c)
            else:
                current_length = len(mylist)
                repeated_c_index = mylist.index(c)
                del mylist[:repeated_c_index+1]
                if max_length < current_length:
                    max_length = current_length
                mylist.append(c)

        return max(max_length,len(mylist))


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("c"))
print(s.lengthOfLongestSubstring(" "))



