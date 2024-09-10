# Combinations

def combine(self, n, k):
    res = []

    def backtrack(nums, k, index, path):
        #if k < 0:  #backtracking
            #return 
        if k == 0:
            res.append(path)
            return # backtracking 
        for i in range(index, len(nums)):
            backtrack(nums, k - 1, i + 1, path + [nums[i]])

    backtrack(range(1, n + 1), k, 0, [])
    return res

# ----------------------------------------------------------------------------
# Permutations I

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(nums, path):
        if not nums:
            res.append(path)
            #return # backtracking
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:], path + [nums[i]])

    backtrack(nums, [])
    return res

# ----------------------------------------------------------------------------
# Permutations II

def permuteUnique(self, nums):
    res, visited = [], [False] * len(nums)
    nums.sort()

    def backtrack(nums, visited, path):
        if len(nums) == len(path):
            res.append(path)
            return 
        for i in range(len(nums)):
            if not visited[i]: 
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                    continue
                visited[i] = True
                backtrack(nums, visited, path + [nums[i]])
                visited[i] = False

    backtrack(nums, visited, [])
    return res

# ----------------------------------------------------------------------------
# Subsets 1

def subsets1(self, nums):
    res = []

    def backtrack(index, path):
        res.append(path)
        for i in range(index, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res

# ----------------------------------------------------------------------------
# Subsets II

def subsetsWithDup(self, nums):
    res = []
    nums.sort()

    def backtrack(nums, index, path):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            backtrack(nums, i + 1, path + [nums[i]])

    backtrack(nums, 0, [])
    return res

# ----------------------------------------------------------------------------
# Combination Sum

def combinationSum(self, candidates, target):
    res = []
    candidates.sort()

    def backtrack(nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            backtrack(nums, target - nums[i], i, path + [nums[i]])

    backtrack(candidates, target, 0, [])
    return res

# ----------------------------------------------------------------------------
# Combination Sum II

def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()

    def backtrack(candidates, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            backtrack(candidates, target - candidates[i], i + 1, path + [candidates[i]])

    backtrack(candidates, target, 0, [])
    return res
