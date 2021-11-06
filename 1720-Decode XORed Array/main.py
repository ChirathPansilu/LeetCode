class Solution:
    # Time O(n) | Space O(n) 
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        for i in encoded:
            output.append(i^first)
            first = output[-1]
        return output