nums = [1,8,6,2,5,4,8,3,7]
k = 3 # Window size
left = 0
ans = []

for right in range(len(nums)):
	# Code using nums[right] to update the state 
	ans.append(nums[right])

	# Condition if window is broken (eg. too long)
	while right - left + 1 > k:
		ans.remove(nums[left])
		left += 1
	
	print(ans)