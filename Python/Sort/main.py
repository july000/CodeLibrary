import random
from Python.Sort.selectSort import select_sort
from mergeSort import merge_sort
from quickSort import quick_sort
from selectSort  import select_sort
from bubbleSort import bubble_sort
from insertSort import insert_sort
from quickSort import quick_sort
length = 10
nums = [random.randint(0, length) for i in range(length)]
print("origin nums: ", nums)
# merge_sort(nums)
# quick_sort(nums)
# select_sort(nums)
# bubble_sort(nums)
# insert_sort(nums)
quick_sort(nums)
print("sorted nums: ", nums)