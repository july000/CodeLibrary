#include <cstring>
#include <algorithm>
class myString
{
    public:
    // myString(){}; // default
    myString(const myString& s); //copy  conctr
    myString(const char* s); // c-string

    ~myString(){};

    myString& operator=(myString& str);

    size_t size()const;
    size_t length();
    size_t max_size();
    void resize();
    size_t capacity()const;
    void reserve(size_t n);

    void clear();
    bool empty()const;
    void shrink_to_fit();

    //element access
    char& operator[](size_t pos);
    const char& operator[](size_t pos) const;
    char& at(size_t pos);
    const char& at(size_t pos) const;
    char& back(size_t pos);
    char& front(size_t pos);

    //modifier
    myString& operator+=(const myString& str);
    myString& operator+=(const char* s);
    myString& operator+=(char c);
    // myString& operator+=(initializer_list<char> il);

    void append(const myString& str);
    void append(const myString& str, size_t subpos, size_t sublen);
    void append(const char* s);
    void append(const char* s, size_t n);
    void append(size_t n, char c);

    myString& assign(const myString& str);
    myString& assign(const myString& str, size_t subpos, size_t sublen);
    myString& assign(const char* s);
    myString& assign(const char* s, size_t n);
    myString& assign(size_t n, char c);

    myString& replace (size_t pos, size_t len, const myString& str);
    // myString& replace (const_iterator i1, const_iterator i2, const myString& str);

    myString& insert(size_t pos, const myString& str);
    myString& insert(size_t pos, const char* c);


    void push_back(char c);
    void pop_back();
    void swap(myString& str);
    myString& erase(size_t pos = 0, size_t len = npos);
    // ierator erase(const_iterator p);
    // iterator erase(const_iterator first, const_iterator last);


    private:
    char* _str; // 指向动态开辟的空间
    size_t _size; // 有效数据的个数
    size_t _capacity; // 容量

    public:
    const static size_t npos;


};