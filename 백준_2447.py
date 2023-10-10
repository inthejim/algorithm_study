def recursive(n,matrix,start_x,start_y):
    if(n==3):
        for i in range(3):
            for j in range(3):
                if(i==1 and j==1):
                    continue;
                matrix[start_x+i][start_y+j]=1
        return
    else:
        for i in range(3):
            for j in range(3):
                if(i==1 and j==1):
                    continue;
                recursive(n//3, matrix, start_x+i*(n//3),start_y+j*(n//3))
    return
n=int(input());
matrix=list(list(0 for i in range(n)) for j in range(n))
recursive(n,matrix,0,0)
for i in range(n):
    for j in range(n):
        if(matrix[i][j]==1):
            print("*", end="")
        else:
            print(" ", end="")
    print();


