while True:
    try:
        shuzi = int(input("请输入一个整数："))
        for i in range(shuzi, 0, -1):
            print(' '*(shuzi - i) + '*'*(2*i - 1))
    except ValueError:
        print("请输入数字")
        
        
        
