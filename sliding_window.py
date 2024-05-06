nums = [1,8,6,2,5,4,8,3,7]
k = 3 # Window size
left = 0
ans = []

for right in range(len(nums)):
	# Check + Solve condition for window (Left pointer) (eg. too long)
	while right - left + 1 > k:
		ans.remove(nums[left])
		left += 1

	# Process element at Right index
	ans.append(nums[right])
	print(ans) # Window content for each loop