"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        nIntermediate = numRows-2 if numRows > 2 else 0
        # first row = multiples of numRows+nIntermediate
        # second row = first down, last diag
        # third row = second down, second to last diag
        # ...
        # last row = multiples of numRows+nIntermediate
        solStr = ''
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                j = i
                while j < len(s):
                    # print only vertical
                    solStr += s[j]
                    j += nIntermediate+numRows
            else:
                j = i
                while j < len(s):
                    # print both vertical and diagonal
                    solStr += s[j]
                    j += (numRows-i) + (nIntermediate-i)
                    if j >= len(s):
                        continue
                    solStr += s[j]
                    j += 2*i
        return solStr