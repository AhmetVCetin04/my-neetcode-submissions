'''
Alright, my current idea is having l and r, where l represents 0 and r represents x
if m == (l + (r - l) // 2) **2 is greater than x, then bring r down to m, if instead m**2 is less than x, bring l up to m + 1
do this until we have the value
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l < r:
            m = l + ((r - l) // 2)
            print(l, m, r)
            if x == m**2 or (m**2 < x and (m+1)**2 > x):
                return m
            elif x > m**2:
                l = m + 1
            else:
                r = m

        return r