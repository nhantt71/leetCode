class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        k = 0
        i = 0
        col = 0
        save = []
        for j in range(n - 1):
            for (x, y) in zip(strs[i], strs[i + 1]):
                if not x <= y and col not in save:
                    k += 1
                    save.append(col)
                if not col + 1 == len(strs[i]):
                    col += 1
            col = 0
            i += 1
        return k