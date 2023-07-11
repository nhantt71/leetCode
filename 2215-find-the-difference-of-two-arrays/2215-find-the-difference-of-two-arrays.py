class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = [x for x in nums1 if x in nums2]
        nums1 = [x for x in nums1 if x not in nums3]
        nums2 = [x for x in nums2 if x not in nums3]
        answer = []
        answer.append(nums1)
        answer.append(nums2)
        return answer

