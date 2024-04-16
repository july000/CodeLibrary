def select_sort(nums):
  n = len(nums)
  for i in range(n):
    min_index = i
    min_val = nums[i]
    for j in range(i+1, n):
      if nums[j] < min_val:
        min_index = j
        min_val = nums[j]
    nums[i], nums[min_index] = nums[min_index], nums[i]

    