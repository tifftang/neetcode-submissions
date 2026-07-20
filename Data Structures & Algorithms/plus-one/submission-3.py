class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = True
        digits.reverse()
        for d in digits:
            val = d
            if carry:
                val = d + 1
            if val > 9:
                val = 10 - val
            else:
                carry = False
            result.append(val)
        if carry:
            result.append(1)
        result.reverse()
        return result