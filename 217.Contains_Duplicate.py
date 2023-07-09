class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)
        return False
