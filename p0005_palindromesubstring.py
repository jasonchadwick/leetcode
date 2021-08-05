"Given a string s, return the longest palindromic substring in s."

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        bestlen1 = 0
        beststr1 = ""
        for c in range(len(s)):
            curlen = 1
            curstr = s[c]
            if curlen > bestlen1:
                bestlen1 = curlen
                beststr1 = curstr
            offset = 1
            while c - offset >= 0 and c + offset < len(s):
                if s[c-offset] == s[c+offset]:
                    curlen += 2
                    curstr = s[c-offset] + curstr + s[c+offset]
                    offset += 1
                else:
                    break
                if curlen > bestlen1:
                    bestlen1 = curlen
                    beststr1 = curstr
        
        bestlen2 = 0
        beststr2 = ""
        for c in range(len(s)-1):
            if s[c] == s[c+1]:
                curlen = 2
                curstr = s[c] + s[c+1]
                if curlen > bestlen2:
                    bestlen2 = curlen
                    beststr2 = curstr
            else:
                continue
            offset = 1
            while c-offset >= 0 and c+offset+1 < len(s):
                if s[c-offset] == s[c+offset+1]:
                    curlen += 2
                    curstr = s[c-offset] + curstr + s[c+offset+1]
                    offset += 1
                else:
                    break
            if curlen > bestlen2:
                bestlen2 = curlen
                beststr2 = curstr
        return beststr1 if bestlen1 > bestlen2 else beststr2
