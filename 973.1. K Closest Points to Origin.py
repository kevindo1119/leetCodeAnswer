class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        """
        Sort use key lambda function
        """
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
