def insert_sort(nums):
  n = len(nums)
  for i in range(1, n):
    j = i-1
    val = nums[i]
    while j >= 0 and nums[j] > val:
      nums[j+1] = nums[j]
      j -= 1
    nums[j+1] = val


