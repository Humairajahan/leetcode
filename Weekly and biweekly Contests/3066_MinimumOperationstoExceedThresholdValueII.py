from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq

        heap = []
        operation = 0

        for num in nums:
            heapq.heappush(heap, num)

        while len(heap) > 2 and heap[0] < k:
            operation += 1
            addition = 2 * heapq.heappop(heap) + heapq.heappop(heap)
            heapq.heappush(heap, addition)

        if heap[0] < k:
            operation += 1

        return operation
