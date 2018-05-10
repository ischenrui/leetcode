# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        ts = ''
        l = 0
        for k in s:
            if ts.find(k) == -1:
                ts += k
                j += 1
            else:

                i = i + 1 + ts.find(k)
                ts = ts[ts.find(k) + 1:] + k
            if len(ts) > l: l = len(ts)

        return l

        """
        d = {}
        rlen = 0
        start = 0
        for index, ch in enumerate(s):
            if ch in d and d[ch]>=start:

                start = d[ch] + 1
            else:
                rlen = max(rlen,index - start+1)
            d[ch] = index
        return rlen
        """