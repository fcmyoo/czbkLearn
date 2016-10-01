# 作业1

userName = 'admin'
password = '888888'
while True:
    userNameInput = input('请输入用户名:')
    if userNameInput == userName:
        passwordInput = input('请输入密码:')
        if passwordInput == password:
            print('欢迎进入XXX的世界!')
            break
        else:
            print('密码不正确!')
            continue
    else:
        print('用户名不正确')
        continue
# 作业2
i = 0
while i < 10:
    if i < 5:
        j = 0
        while j <= i:
            print('*', end='')
            j += 1
        print()
    else:
        k = 10
        while k >= i:
            print('*', end='')
            k -= 1
        print()
    i += 1
