import os

#
# print ("目录为: %s"%os.listdir(os.getcwd()))
# # os.rename('345.txt','abc.txt')
# # os.remove('abc.txt')
#
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

# pathDir = os.path.exists('movies')
# if not pathDir:
#     os.mkdir('movies')
# i = 1
# getDir=os.getcwd()
#
# while i < 10:
#     newFile=getDir+'/movies/新三国' + str(i) + '.txt'
#     with open(newFile,'w+') as f:
#         f.write('')
#     i += 1
#

# print(os.chdir(os.getcwd()+ '/movies'))

os.chdir('movies')
filePaht=os.listdir(os.getcwd())
for i in filePaht:
    a1=i.split('.')
    editName='[xxx出票]-'+a1[0]+'.'+a1[-1]
    with open(editName,'w+') as f:
        f.write('')


# oldFileName = input('请输入你复制的文件名字:')
# # 打开
# with open(oldFileName, 'r+') as oldFile:
#     num = oldFileName.find('.')
#     a1 = oldFileName[0:num]
#     a2 = oldFileName[num:]
#     newFileNme = a1 + '[复件]' + a2
#     with open(newFileNme, 'w+') as newFile:
#         content = oldFile.readline()
#         while len(content) > 0:
#             newFile.write(content)
#             content = oldFile.readline()
