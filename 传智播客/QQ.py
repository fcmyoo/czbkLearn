from socket import *
import threading

recv_data = ()
# 一个线程完成收数据
class RecvData(threading.Thread):
    def run(self):
        recv_data = s.recvfrom(1024)
        print(recv_data[0])


# 一个线程完成发数据
class SendData(threading.Thread):
    def run(self):
        send_Data = input('请输入要发送的内容:')
        s.sendto(send_Data)


# 创建socket
s = socket(AF_INET, SOCK_DGRAM)
bing_addr=('',8080)
s.bind(bing_addr)

# 创建发线程
rThread = RecvData()
rThread.start()
# 创建收线程
sThread = SendData()
sThread.start()


rThread.join()
sThread.join()

# 关闭socket
s.close()
