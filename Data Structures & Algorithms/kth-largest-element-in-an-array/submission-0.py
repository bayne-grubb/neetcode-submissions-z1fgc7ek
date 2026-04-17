class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = heapq.nlargest(k, nums)[-1]
        return kth