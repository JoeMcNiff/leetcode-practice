class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = 1
        t = len(s)
        if t == 0:
            return 0
        for i, l in enumerate(s):
            letters = [l]
            r = 1
            while ((i+r) < t):
                if s[i+r] not in letters:
                    letters.append(s[i+r])
                    r+=1
                    continue
                break
            if r > record:
                record = r
        return record




            
        
        
        
    
        