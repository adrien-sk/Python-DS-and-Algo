class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        dictionary1, dictionary2 = {}, {}
        
        for i in range(len(s)):
                dictionary1[s[i]] = 1 + dictionary1.get(s[i], 0)
                dictionary2[t[i]] = 1 + dictionary2.get(t[i], 0)

        for key in dictionary1:
            if dictionary1[key] != dictionary2.get(key,0):
                return False
        return True
