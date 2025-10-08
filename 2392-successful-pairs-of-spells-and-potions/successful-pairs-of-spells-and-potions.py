from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            # Minimum potion strength needed for success
            min_potion = (success + spell - 1) // spell  # ceiling division

            # Binary search to find first potion ≥ min_potion
            index = bisect_left(potions, min_potion)

            # Number of successful potions for this spell
            result.append(m - index)

        return result
