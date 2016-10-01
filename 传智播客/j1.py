import threading
from queue import Queue
from time import sleep


sleep(1)
b = threading.Thread


# # --------------练习-----------------------------------------------
# class P(threading.Thread):
#     def run(self):
#         num = 100
#         while True:
#             if queue.qsize() < 1000:
#                 for i in range(5):
#                     shaobin = '-生产了烧饼' + str(num)
#                     queue.put(shaobin)
#                     print(shaobin)
#                     num += 1
#             sleep(1)
#
#
# class C(threading.Thread):
#     def run(self):
#         while True:
#             if queue.qsize() > 100:
#                 for i in range(3):
#                     shaobin = queue.get()
#                     print('---消费了烧饼--%s' % shaobin)
#             sleep(1)
#
#
# queue = Queue()
# for i in range(500):
#     queue.put('武大郎烧饼%d' % i)
#
# c = C()
# c.start()
# p = P()
# p.start()

# --------------------队列-------------------------
# import threading
# from queue import Queue
# from time import sleep
#
# class P(threading.Thread):
#     def run(self):
#         while True:
#             if queue.qsize() < 1000:
#                 num = 500
#                 for i in range(5):
#                     shaobin='生产了武大郎烧饼'+str(num)
#                     queue.put(shaobin)
#                     print(shaobin)
#                     num += 1
#             sleep(1)
#
# class C(threading.Thread):
#     def run(self):
#         while True:
#
#             if queue.qsize() > 100:
#                 for i in range(3):
#                     shaobin = queue.get()
#                     print('-----消费了 %s----'%shaobin)
#             sleep(1)
#
# queue = Queue()
# for i in range(500):
#     queue.put('武大郎烧饼-%d' % i)
#
# p = P()
# p.start()
# c = C()
# c.start()

# ----------------------------------------1----------------------
import threading
import time

# # # def sing():
# # #     for i in range(3):
# # #         print('正在唱个歌..%d' % i)
# # #         time.sleep(1)
# # #
# # #
# # # def dance():
# # #     for i in range(3):
# # #         print('正在跳舞..%d' % i)
# # #         time.sleep(1)
# # # # def chuifeng():
# # # #     for i in range(3):
# # # #         print('正在吹风..%d' % i)
# # # #         sleep(1)
# # #
# # # def saySorry():
# # #     print('sorry.....')
# # #     time.sleep(1)
# #
# #
# # class MyThread(threading.Thread):
# #     global num
# #     num = 0
# #     global mutex
# #     mutex = threading.Lock()
# #
# #     def run(self):
# #         # for i in range(3):
# #         #     time.sleep(1)
# #         #     msg = "I'm" + self.name + ' @ ' + str(i)
# #         #     print(msg)
# #        if mutex.acquire(1):
# #            global num
# #            num += 1
# #            time.sleep(0.5)
# #            msg = self.name + ' set num to ' + str(num)
# #            print(msg)
# #            mutex.release()
# #
# # def test():
# #     for i in range(5):
# #         t = MyThread()
# #         t.start()
#
# # 死锁
# mutexA = threading.Lock()
# mutexB = threading.Lock()
#
#
# class MyThread1(threading.Thread):
#     def run(self):
#         if mutexA.acquire():
#             print(self.name + '----do1---up---')
#             time.sleep(1)
#             if mutexB.acquire():
#                 print(self.name + '----do1---down---')
#                 time.sleep(1)
#                 mutexB.release()
#             mutexA.release()
#
#
# class MyThread2(threading.Thread):
#     def run(self):
#         if mutexB.acquire():
#             print(self.name + '----do2---up---')
#             time.sleep(1)
#             if mutexA.acquire():
#                 print(self.name + '----do2---down---')
#                 time.sleep(1)
#                 mutexA.release()
#             mutexB.release()
#
#
# if __name__ == '__main__':
#     # print('===开始----', ctime())
#     # threading._start_new_thread(sing, ())
#     # threading._start_new_thread(dance, ())
#     # threading._start_new_thread(chuifeng, ())
#     # # sleep(3)
#     # print('over',ctime())
#     # for i in range(5):
#     #     t=threading.Thread(target=saySorry)
#     #     t.start()
#     # t1=threading.Thread(target=dance)
#     # t2=threading.Thread(target=sing)
#     # t1.start()
#     # t2.start()
#     #
#     # test()
#     t1 = MyThread1()
#     t2 = MyThread2()
#     t1.start()
#     t2.start()
