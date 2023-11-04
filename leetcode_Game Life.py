import copy

class Solution:
    dx=[1,1,1,-1,-1,-1,0,0]
    dy=[1,-1,0,1,-1,0,1,-1]
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_board=[[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count=0
                for k in range(8):
                    ni=i+self.dx[k]
                    nj=j+self.dy[k]
                    if(0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj]==1):
                        count+=1
                temp_board[i][j]=count


        for i in range(len(board)):
            for j in range(len(board[0])): 
                if(board[i][j]==1):
                    if(2<=temp_board[i][j]<=3):
                        board[i][j]=1
                    else:
                        board[i][j]=0
                
                elif(board[i][j]==0 and temp_board[i][j]==3):
                    board[i][j]=1
     
        
