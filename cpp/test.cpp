#include <thread>
#include <iostream>
#include <atomic>  // 需要这个库支持原子变量

// 创建一个原子布尔变量作为退出信号
std::atomic<bool> stop(false);

void threaded_function() {
    static int counter = 0;
    while (!stop) {  // 检查退出信号
        counter++;
        std::cout << "Counter: " << counter << "\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(10));  // 休眠一会儿
    }
}

int main() {
    while (true) {
      int cn = 0;
      std::thread t(threaded_function);  // 创建并启动线程
      while (true) {
          cn++;
          // 假设这是你的某个退出条件
          if (cn > 5) {
              stop = true;  // 设置退出信号
              t.
              break;  // 跳出嵌套的while循环
          }
      }
      
    }

    t.join();  // 等待线程结束
    return 0;
}