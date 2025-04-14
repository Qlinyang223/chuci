for shuzi in range(100,1000):
    sxh = shuzi
    bai = sxh // 100
    shi = (sxh // 10) % 10
    ge = sxh % 10
    if bai ** 3 + shi ** 3 + ge ** 3 == sxh:
        print(f"{sxh}是水仙花数")
        
