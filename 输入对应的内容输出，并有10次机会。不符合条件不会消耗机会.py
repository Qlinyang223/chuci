count = 10
while count > 0:
    try:
        shuzi = input("请输入1到100的数字：")
        shuzi = int(shuzi)
        if 1 <= shuzi <= 100:
            print("你妹妹好漂亮！")
        else:
            print("你大爷好丑。")
        count -= 1
    except ValueError:
        print("请输入数字")
        continue
        
