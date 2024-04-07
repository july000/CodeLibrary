#include <iostream>
#include <vector>

// https://stackoverflow.com/questions/5232198/how-does-the-capacity-of-stdvector-grow-automatically-what-is-the-rate
// vector 的扩容是以1.5倍增长的
int main()
{
	std::vector<int> v;
	for (int i = 0; i < 100; i++)
	{
		std::cout << "v.capcaity : " << v.capacity() << ", v.size : " << v.size() << std::endl;
		v.push_back(i);
	}
	return 0;
}