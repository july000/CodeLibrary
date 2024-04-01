#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;
int counter = 1;

void printNumbers(int threadID, int maxCount) {
    while(true) {
        mtx.lock();
        if(counter > maxCount) {
            mtx.unlock();
            return;
        }
        if(counter % 3 == threadID) {
            std::cout << "Thread " << threadID + 1 << ": " << counter++ << std::endl;
        }
        mtx.unlock();
    }
}

int main() {
    const int MAX_COUNT = 100;

    std::thread t1(printNumbers, 0, MAX_COUNT);
    std::thread t2(printNumbers, 1, MAX_COUNT);
    std::thread t3(printNumbers, 2, MAX_COUNT);

    t1.join();
    t2.join();
    t3.join();

    return 0;
}
