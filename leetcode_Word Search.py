class Solution:
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    def dfs(self, board: List[List[str]], i:int, j:int, word:str, idx:int)->bool:
        
        if(not (0<=i<len(board) and 0<=j<len(board[0]))):
            return False
        if(word[idx]!=board[i][j]):
            return False
        if(idx==len(word)-1):
            return True
        
        tmp=board[i][j]
        board[i][j]=-1

        for k in range(4):
            ni=i+self.dx[k]
            nj=j+self.dy[k]
            
            if(self.dfs(board, ni, nj, word, idx+1)):
                return True

        board[i][j]=tmp
           
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.dfs(board,i,j,word,0)):
                    return True
                
        return False
