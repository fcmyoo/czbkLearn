from socket import *

# 创建socket
serSocket=socket(AF_INET,SOCK_STREAM)
# 设置服务器地址和端口
localAddr=('',7890)
# 绑定服务器地址和端口
serSocket.bind(localAddr)

# 设置监听
serSocket.listen(5)
# 接收信息
newSocket,destAddr=serSocket.accept()
print(destAddr,newSocket)
# 接收对方发送过来的数据
recvData=newSocket.recv(1024)
print(recvData)
# 发送数据给对方
newSocket.send(b'3q')

newSocket.close()
serSocket.close()
