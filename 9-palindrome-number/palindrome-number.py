class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xs = str(x)
        w = 0
        y = len(xs)-1
        while w < y:
            if xs[w] != xs[y]:
                return False
            w += 1
            y -= 1
        return True


        