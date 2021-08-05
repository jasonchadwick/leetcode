class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xnew = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            x,digit = divmod(x, 10)
            xnew *= 10
            xnew += digit
            if xnew < 0 or xnew > 2**31-1 or xnew < -2**31:
                return 0
        return xnew * sign