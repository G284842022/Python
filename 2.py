def stars(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("★", end=" ")
            else:
                print("☆", end=" ")
        print()
        
stars(5)