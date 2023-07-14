class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def get_max_value(sublist):
            return sublist[k]

        score.sort(key=get_max_value, reverse=True)
        return score