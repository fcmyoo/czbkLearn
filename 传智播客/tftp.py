import struct
from socket import *

# 1.创建套接字
s = socket(AF_INET, SOCK_DGRAM)
# 1.1组装发送的数据
requestData = struct.pack(b'!H8sb5sb', 1, b'test.jpg', 0, b'octet', 0)
# 2.发送请求
s.sendto(requestData, ('192.168.0.36', 69))
# 3.循环接收数据
while True:
    # 3.1接收数据
    recvData, destAddr = s.recvfrom(1024)
    # 3.1.1从接收的数据中提取出想要的数据

    # 3.1.2解析出序号,比如(3,1)
    cmdTuple = struct.unpack(b'!HH', recvData[:4])
    # 操作码
    cmdKey = cmdTuple[0]
    if cmdKey == 3:
        # 序号
        packNum = cmdTuple[1]
        print('-----%d-----' % packNum)
        if packNum == 1:
            writeFile=open('test.jpg','wb')
        # 3.1.3组装确认包
        ackData = struct.pack(b'!HH', 4, packNum)
        # 3.2发送确认信息给对方
        s.sendto(ackData, destAddr)
        # 3.3保存接收的数据
        writeFile.write(recvData[4:])
        if len(recvData) < 516:
            writeFile.close()
            break
    if cmdKey == 5:
        print('---出现了错误---')
        break
s.close()
