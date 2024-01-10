#include <iostream>

void byValue(int x)
{
    x = 10;
}

void byReference(int& x)
{
    
    x = 20;
}

void byPointer(int* x)
{
    *x = 30;
}


void moveSemantics(int&& x)
{
    x = 40;
}

int main() {
    int a = 5;
    byValue(a);
    std::cout << "After byValue : " << a << std::endl;
    
    byReference(a);
    std::cout << "After byReference : " << a << std::endl;
    
    byPointer(&a);
    std::cout << "After byPointer : " << a << std::endl;
    
    moveSemantics(std::move(a));
    std::cout << "After moveSemantics : " << a << std::endl;

    return 0;
}
