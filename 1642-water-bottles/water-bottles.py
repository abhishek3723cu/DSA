class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            newBottles = empty // numExchange   # how many full bottles you get
            total += newBottles                 # drink them
            empty = empty % numExchange + newBottles  # leftovers + new empties
            
        return total
