#include <iostream>
//如果在基类的声明中带有默认实参值，则通过基类指针调用该函数时，就总是从函数的基类版本中接受默认实参值
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