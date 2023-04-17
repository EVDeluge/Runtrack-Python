def draw_diagonal(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j or i+j == n:
                print("*", end="")
            else:
                print("-", end="")
        print()