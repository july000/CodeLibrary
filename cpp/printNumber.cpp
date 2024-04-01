#include <iostream>
#include <thread>

// 打印数字的线程函数
void printNumbers(int start, int end) {
    for (int i = start; i <= end; ++i) {
        std::cout << i << " ";
    }
}

int main() {
    // 创建三个线程，并分别指定打印的范围
    std::thread thread1(printNumbers, 1, 33);
    std::thread thread2(printNumbers, 34, 66);
    std::thread thread3(printNumbers, 67, 100);

    // 等待每个线程执行完毕
    thread1.join();
    thread2.join();
    thread3.join();

    return 0;
}
