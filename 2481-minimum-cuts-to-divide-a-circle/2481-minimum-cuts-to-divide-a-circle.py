class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            m = n / 2
        elif n == 1:
            m = 0
        else:
            m = n
        return int(m)