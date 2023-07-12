class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        candyType = list(set(candyType))
        if len(candyType) >= n / 2:
            return n / 2
        else:
            return len(candyType)