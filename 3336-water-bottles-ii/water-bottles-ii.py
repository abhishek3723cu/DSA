class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            # exchange once
            empty -= numExchange
            total += 1
            empty += 1   # new empty bottle after drinking
            numExchange += 1  # exchange cost increases
        
        return total
