def insert_sort(nums):
    # 区分有序部分与无序部分
    n = len(nums)
    if n < 2:
        return
    for i in range(1, n):
        val = nums[i]
        j = i-1
        while j >= 0 and nums[j] > val:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = val



def bubble_sort(nums):
    # 依次比较相邻的两个数字，大数放在后面, 先确定最大值
    n = len(nums)
    if n < 2:
        return
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if nums[j]>nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    

def select_sort(nums):
    # 从i-N中选择一个最小的放在第i位
    n = len(nums)
    if n < 2:
        return
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [2,1,4,7,3,9,6,8,13, 12,14,1,2]
# select_sort(nums)
# bubble_sort(nums)
insert_sort(nums)

print(nums)
