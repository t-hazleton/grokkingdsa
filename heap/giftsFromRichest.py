import heapq  # Importing the heapq module for efficient heap operations
import math

class Solution:
    def __init__(self):
        self = self

    def remainingGifts(self, gifts, k):
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        while k:
            pile = heapq.heappop(gifts)
            newPile = math.sqrt(-pile)
            heapq.heappush(gifts, -int(newPile))
            k -= 1
        return -sum(gifts)

gifts = [4, 9, 16]
solution = Solution().remainingGifts(gifts, 2)
print(solution)