#include <cstring>
#include <iostream>

int main()
{
  char src[] = "hello world";
  char dst[6];
  std::memcpy(dst, src, sizeof(dst));
  std::cout << "addr src : " << &src << ", addr dst : " << &dst << std::endl;
}