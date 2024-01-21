#include "myString.h"
using namespace std;

// myString::myString(){}; // default
myString::myString(const myString& str="")
{
    _str = new char[str._capacity + 1];
    strcpy(_str, str._str); // char* strcpy(char* dest, const char* src);
    _size = str._size;
    _capacity = str._capacity;
}

myString::myString(const char* c):_size(strlen(c)), _capacity(_size)
{
    _str = new char[_capacity + 1];
    strcpy(_str, c);
}
myString::~myString()
{
    delete[] _str;
    _size = 0;
    _capacity = 0;
    _str = nullptr;
};

myString& myString::operator=(myString& str)
{
    if(this != &str)
    {
        char* tmp = new char[str._capacity + 1];
        strcpy(tmp, str._str);
        delete[] _str;
        _str = tmp;
        _size = str._size;
        _capacity = str._capacity;

    }
    return *this;
}

char& myString::operator[](size_t pos)
{
    return _str[pos];
}

size_t myString::size()const
{
    return _size;
}

bool myString::empty()const{
    return _size == 0;
}
size_t myString::capacity()const{
    return _capacity;
}

void myString::reserve(size_t n)
{
    if (n > _capacity)
    {
        char* tmp = new char[n + 1];
        strcpy(tmp, _str);
        delete[] _str;
        _capacity = n;
        _str = tmp;
    }
}

void myString::push_back(char c)
{
    if (_capacity == _size)
    {
        reserve(_capacity == 0? 4 : _capacity * 2);
    }
    _str[_size] = c;
    _size++;
    _str[_size] = '\0';
}

void myString::append(const char* str)
{
    size_t len = strlen(str);
    if(len + _size >= _capacity)
    {
        reserve(len + _size);
    }
    strcpy(_str+_size, str);
    _size += len;
}

myString& myString::operator+=(const char* s)
{
    append(s);
    return *this;
}


myString& myString::operator+=(char c)
{
    push_back(c);
    return *this;
}


void myString::swap(myString& str)
{   
    std::swap(_str, str._str);
    std::swap(_size, str._size);
    std::swap(_capacity, str._capacity);
}

void myString::clear()
{
    //将有效数据个数设置为0，并不用释放空间
    _str[0] = '\0';
    _size = 0;
}