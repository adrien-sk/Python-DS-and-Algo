# Combinations

def combine(self, n, k):
    res = []

    def dfs(nums, k, index, path):
        #if k < 0:  #backtracking
            #return 
        if k == 0:
            res.append(path)
            return # backtracking 
        for i in range(index, len(nums)):
            dfs(nums, k - 1, i + 1, path + [nums[i]])

    dfs(range(1, n + 1), k, 0, [])
    return res

# ----------------------------------------------------------------------------
# Permutations I

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(nums, path):
        if not nums:
            res.append(path)
            #return # backtracking
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path + [nums[i]])

    dfs(nums, [])
    return res

# ----------------------------------------------------------------------------
# Permutations II

def permuteUnique(self, nums):
    res, visited = [], [False] * len(nums)
    nums.sort()

    def dfs(nums, visited, path):
        if len(nums) == len(path):
            res.append(path)
            return 
        for i in range(len(nums)):
            if not visited[i]: 
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                    continue
                visited[i] = True
                dfs(nums, visited, path + [nums[i]])
                visited[i] = False

    dfs(nums, visited, [])
    return res

# ----------------------------------------------------------------------------
# Subsets 1

def subsets1(self, nums):
    res = []

    def dfs(nums, index, path):
        res.append(path)
        for i in range(index, len(nums)):
            dfs(nums, i + 1, path + [nums[i]])

    dfs(sorted(nums), 0, [])
    return res

# ----------------------------------------------------------------------------
# Subsets II

def subsetsWithDup(self, nums):
    res = []
    nums.sort()

    def dfs(nums, index, path):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            dfs(nums, i + 1, path + [nums[i]])

    dfs(nums, 0, [])
    return res

# ----------------------------------------------------------------------------
# Combination Sum

def combinationSum(self, candidates, target):
    res = []
    candidates.sort()

    def dfs(nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            dfs(nums, target - nums[i], i, path + [nums[i]])

    dfs(candidates, target, 0, [])
    return res

# ----------------------------------------------------------------------------
# Combination Sum II

def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()

    def dfs(candidates, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])

    dfs(candidates, target, 0, [])
    return res