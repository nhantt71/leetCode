class Solution:
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def findPairs(n):
            if n == 1:
                return 0
            else:
                return (n - 1) + findPairs(n - 1)

        d = {}
        for i in range(len(words)):
            words[i] = "".join(set(words[i]))
        for x in words:
            if x not in d.keys():
                d[x] = 1
            else:
                d[x] += 1
        count = 0
        for x in d.values():
            count += findPairs(x)
        return count