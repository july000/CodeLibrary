#include <iostream>
#include <string>
#include <unordered_set>
#include <cmath>

int main()
{
  std::string str = "";
  std::unordered_set<char> set;
  int left = 0;
  int res = 0;
  int maxLength = 0;
  if (str.empty())
  {
    printf("maxLength : %d\n", maxLength);
    return maxLength;
  }
  for (int right = 0; right < str.size(); right++)
  {
    while (set.find(str[right]) != set.end())
    {
      set.erase(str[left++]);
    }
    set.insert(str[right]);
    maxLength = std::max(maxLength, right-left+1);
  }
  printf("maxLength : %d\n", maxLength);
  return maxLength;
}