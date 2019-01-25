class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        """
        Sort use priority queue (use heapq to implement)
        """
        priority_q = []
        
        for point in points:
            heapq.heappush(priority_q, (point[0]**2 + point[1]**2, point))
        
        num_temp = K
        res = []
        
        while num_temp > 0:
            res.append(heapq.heappop(priority_q)[1])
            num_temp -= 1
            
        return res
