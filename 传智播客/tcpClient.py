from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
# 链接服务器
serAddr = ('192.168.0.36', 7788)
tcpClientSocket.connect(serAddr)
# 提示用户输入的数据
sendData = input(u'请输入要发送的数据:')
tcpClientSocket.send(bytes(sendData, encoding='utf-8'))
# 接收对方发送过来的数据,最大接收1024字节
recvData = tcpClientSocket.recv(1024)

print('接收到的数据为:', recvData)

# 关闭套接字
tcpClientSocket.close()
