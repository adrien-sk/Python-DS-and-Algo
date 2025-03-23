# Combinations

def combine(self, n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(path, index):
        if len(path) == k:
            res.append(path)
            return
        
        for i in range(index, n + 1):
            backtrack(path + [i], i + 1)
    
    backtrack([], 1)
    return res

# ----------------------------------------------------------------------------
# Permutations I

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(nums, path):
        if not nums:
            res.append(path)
            return # backtracking
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:], path + [nums[i]])

    backtrack(nums, [])
    return res

# ----------------------------------------------------------------------------
# Permutations II

# Mutable version (modify Path and Count global variables) ------------------------------
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    count = { n:0 for n in nums }

    for n in nums:
        count[n] += 1
    
    def backtrack():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        
        for n, c in count.items():
            if c > 0:
                path.append(n)
                count[n] -= 1
                backtrack()
                count[n] += 1
                path.pop()
    backtrack()
    return res


# Pure Functional Programing version ------------------------------
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    count = {n: 0 for n in nums}

    for n in nums:
        count[n] += 1

    def backtrack(path, curr_count):
        if len(path) == len(nums):
            res.append(path)
            return

        for n in curr_count:
            if curr_count[n] > 0:
                new_count = curr_count.copy()
                new_count[n] -= 1
                backtrack(path + [n], new_count)

    backtrack([], count)
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

    def backtrack(index, path):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res

# ----------------------------------------------------------------------------
# Combination Sum

def combinationSum(self, candidates, target):
    res = []
    candidates.sort()

    def backtrack(target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(candidates)):
            backtrack(target - candidates[i], i, path + [candidates[i]])

    backtrack(target, 0, [])
    return res

# ----------------------------------------------------------------------------
# Combination Sum II

def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()

    def backtrack(target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            backtrack(target - candidates[i], i + 1, path + [candidates[i]])

    backtrack(target, 0, [])
    return res
