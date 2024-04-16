import random

def quick_sort(nums):
  n = len(nums)
  if n < 2:
    return
  process(nums, 0, n-1)

def process(nums, left, right):
  if left >= right:
    return
  index = random.randint(left, right)
  nums[index], nums[right] = nums[right], nums[index]

  mid = partition(nums, left, right)
  process(nums, left, mid-1)
  process(nums, mid+1, right)

def partition(nums, left, right):
  i = left - 1
  val = nums[right]
  while left < right:
    if nums[left] < val:
      nums[i+1], nums[left] = nums[left], nums[i+1]
      left += 1
      i += 1
    else:
      left += 1
  nums[i+1], nums[right] = nums[right], nums[i+1]
  return i+1
