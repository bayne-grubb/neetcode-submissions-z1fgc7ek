class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [element_count[0] for element_count in Counter(nums).most_common(k)]