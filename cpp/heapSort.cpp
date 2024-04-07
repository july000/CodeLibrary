#include <iostream>
#include <vector>

void heapInsert(std::vector<int>& nums, int index, int heapSize)
{
  while(index < heapSize)
  {
    int parentIndex = (index - 1) / 2;
    if(nums[index] > nums[parentIndex])
    {
      std::swap(nums[index], nums[parentIndex]);
      index = parentIndex;
    }
    else
    {
      break;
    }
  }
}

void heapity(std::vector<int>& nums, int index, int heapSize)
{
  int left = 2 * index + 1;
  while(left < heapSize)
  {
    int largest = nums[left+1] > nums[left] && left+1 < heapSize ? left+1 : left;
    if(nums[index] < nums[largest])
    {
      std::swap(nums[index], nums[largest]);
      index = largest;
      left = 2 * index + 1;
    }
    else
    {
      break;
    }
  }
}

void print_vector(std::vector<int>& nums)
{
  for (int i = 0; i < nums.size(); i++)
  {
    std::cout << nums[i] << ", " ;
  }
  std::cout << std::endl;
}

int main()
{
  std::vector<int> nums = {9,8,7,6,5,4,3,2,1};
  int heapSize = 0;
  for (int i = 0; i < nums.size(); i++)
  {
    heapSize++;
    heapInsert(nums, i, heapSize);
  }
  std::swap(nums[0], nums[nums.size()-1]);
  heapSize--;
  while(heapSize > 0)
  {
    heapity(nums, 0, heapSize);
    std::swap(nums[0], nums[--heapSize]);
  }
  print_vector(nums);

}