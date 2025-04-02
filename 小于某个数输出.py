while True:
    try:
        shuru = input("请输入一个整数：")
        shuzi = int(shuru)
        for sum in range(1,shuzi + 1):
            print(sum)
    except ValueError:
        print("请输入数字")
        continue
