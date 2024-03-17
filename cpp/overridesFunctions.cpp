#include <iostream>
//����ڻ���������д���Ĭ��ʵ��ֵ����ͨ������ָ����øú���ʱ�������ǴӺ����Ļ���汾�н���Ĭ��ʵ��ֵ
//https://zhuanlan.zhihu.com/p/224990704
struct Base
{
	virtual void display(int i = 5)
	{
		std::cout << "Base : i = " << i << std::endl;
	}
};

struct Derived : public Base
{
	virtual void display(int i = 9)
	{
		std::cout << "Derived : i = " << i << std::endl;
	}
};

int main()
{
	Base* a = new Derived();
	a->display();
	
	Base* aa = new Base();
	aa->display();

	Derived* b = new Derived();
	b->display();
}