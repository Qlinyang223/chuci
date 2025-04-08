count = 10
while count > 0:
    try:
        nianfen = input("请输入年份:")
        shuzi = int(nianfen)
        if shuzi % 4 == 0 and shuzi != 0 or shuzi % 400 == 0:
            print("是闰年")
        else:
            print("是平年")
        count = count - 1
    except ValueError:
        print("请输入数字：")
        continue



