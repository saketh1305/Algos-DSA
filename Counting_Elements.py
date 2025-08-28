# Noob developer : O(n^2) => Without Hashset
# With the hashset
from typing import List
class Solution:
    def countElements(self, arr: List[int]):
        s = set(arr)
        count = 0
        for x in arr:
            if x+1 in s:
                count+=1
        return count