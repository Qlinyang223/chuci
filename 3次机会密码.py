password = "林洋"
count = 3
while count > 0:
    input_pwd = input("请输入密码:******")
    if "*" in input_pwd:
        print("密码中不能含有"*"号！您还有",count,"次机会！")
        continue
    if input_pwd == password:
        print("密码正确，进入程序.......")
        break
    else:
        count-= 1
        print("密码输入错误，您还有",count,"次机会")
else:
        print("您的机会已用完")
