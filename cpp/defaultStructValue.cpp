#include <iostream>
#include <string>

struct myStruct
{
    float age;
    float height;
};

int main() {

    
    for (int i = 0; i < 20; i++){
        myStruct student;
        student.age = i;
        
        std::cout << "student.age : " << student.age << std::endl;
        std::cout << "student.height : " << student.height << std::endl;
        std::cout << "address : " << &student << std::endl;

        
    }

            
    return 0;
}