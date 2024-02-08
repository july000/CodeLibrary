#include <iostream>

class Foo
{
public:
	Foo()
	{
		std::cout << "Foo constructer" << std::endl;
		//display();
	}
	virtual void run() const
	{
		std::cout << "Foo run" << std::endl;
	}
	void eat() const
	{
		std::cout << "Foo eat" << std::endl;
	}
	virtual void display()
	{
		std::cout << "Hello Foo!" << std::endl;
	}
	virtual ~Foo(){}
};

class Bar : public Foo
{
public:
	Bar()
	{
		std::cout << "Bar constructer" << std::endl;
	}
	void run() const
	{
		std::cout << "Bar run" << std::endl;
	}
	void eat() const
	{
		std::cout << "Bar eat" << std::endl;
	}
	void display()
	{
		std::cout << "Hello Bar!" << std::endl;
	}
	virtual ~Bar(){}
};

int main()
{
	Foo* f = new Bar();
	f->run();
	f->eat();
	delete f;
	return 0;
}