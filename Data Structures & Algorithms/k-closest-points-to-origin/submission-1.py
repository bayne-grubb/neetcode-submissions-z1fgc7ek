class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(point):
            x, y = point
            return math.sqrt((x**2) + (y**2))
        heap = []
        for point in points:
            dist = distance_from_origin(point)
            heapq.heappush(heap, (dist, point))

        
        return [heapq.heappop(heap)[1] for i in range(k)]
        