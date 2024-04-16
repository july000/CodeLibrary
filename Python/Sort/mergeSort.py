def merge_sort(nums):
  n = len(nums)
  if n < 2:
    return
  process(nums, 0, n-1)

def process(nums, left, right):
  if left == right:
    return
  mid = (left + right) // 2 #当right非常大的时候, 可能会越界
  process(nums, left, mid)
  process(nums, mid+1, right)
  merge(nums, left, mid, right)

def merge(nums, left, mid, right):
  help = [0] * (right - left + 1)
  i = 0
  p1 = left
  p2 = mid + 1
  while p1 <= mid and p2 <= right:
    if nums[p1] <= nums[p2]:
      help[i] = nums[p1]
      p1 += 1
    else:
      help[i] = nums[p2]
      p2 += 1
    i += 1
  if p2 == right+1:
    help[i:] = nums[p1:mid+1] # 注意等号右边不是nums[p1:], 这是将nums数组中的p1之后的所有数字
  if p1 == mid+1:
    help[i:] = nums[p2:right+1]  # # 注意等号右边不是nums[p2:], 这是将nums数组中的p2之后的所有数字

  nums[left:right+1] = help[:]
