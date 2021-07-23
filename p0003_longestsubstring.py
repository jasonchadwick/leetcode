"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_found = 0
        for i,startchar in enumerate(s):
            subs = str(startchar)
            for j in range(i+1,len(s)):
                if s[j] in subs:
                    longest_found = max(longest_found, len(subs))
                    break
                subs += s[j]
            longest_found = max(longest_found, len(subs))
        return longest_found

# better solution: use a dict. Loop through, adding each char if not in dict, and if in dict then calculate length of current substring and start over.
# if this len is longer than current max, set the max to it. O(n).