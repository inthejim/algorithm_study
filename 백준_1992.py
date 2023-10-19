def recursive(matrix, start_x, start_y, n):
    
    standard=matrix[start_x][start_y];
    if(n==1):
        if(standard==0):
            print("0",end="")
        elif(standard==1):
            print("1",end="")
        return
   
    temp=standard
    for i in range(start_x,start_x+n):
        for j in range(start_y,start_y+n):
            if(matrix[i][j]!=standard):
                temp=matrix[i][j]
                break;
        if(temp!=standard):
            break;
    if(standard==temp):
        if(standard==0):
            print("0",end="")
        elif(standard==1):
            print("1",end="")
        return;
    else:
        print("(",end="");
        for i in range(2):
            for j in range(2):
                
                recursive(matrix, start_x+(n//2)*i, start_y+(n//2)*j, n//2);
        print(")",end="");
    
    return

n=int(input());
matrix=list(list(map(int,input().strip())) for i in range(n));
recursive(matrix,0,0,n);
