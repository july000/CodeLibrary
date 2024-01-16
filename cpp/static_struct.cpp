#include <iostream>
// static 变量的默认值是0；
struct Data{
    int a;
    int b;
    int c;
};

int main() {
    // Write C++ code here
    static int var;
    int d;
    printf("default static int : %d", var);
    printf("default int : %d", d);
    static Data data;
    for(int i = 0; i < 5; i++)
    {
        data.a += 1;
        data.b += 10;
        data.c += 100;
        std::cout << "a : " << data.a << ", b : "<< data.b << ", c : " << data.c << std::endl;
    }

    return 0;
}