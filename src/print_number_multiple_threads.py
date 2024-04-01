#import threading
#import time
#
#lock = threading.Lock()
#num = 1
#
#def print_num():
#    global num
#    while num <= 100:
#        lock.acquire()
#        print(num)
#        num += 1
#        lock.release()
#
#t1 = threading.Thread(target=print_num)
#t2 = threading.Thread(target=print_num)
#t3 = threading.Thread(target=print_num)
#
#t1.start()
#t2.start()
#t3.start()
#
#t1.join()
#t2.join()
#t3.join()
import threading

# 定义一个全局的计数器
counter = 1
# 创建一个锁对象
lock = threading.Lock()

def print_numbers(thread_id, max_num):
    global counter
    while True:
        lock.acquire()
        if counter > max_num:
            lock.release()
            break
        if counter % 3 == thread_id:
            print(f'Thread {thread_id}: {counter}')
            counter += 1
        lock.release()

def main():
    # 最大打印的数
    max_num = 100
    # 创建3个线程
    threads = [threading.Thread(target=print_numbers, args=(i, max_num)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__=='__main__':
    main()
