#Author : koder_786
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def check(i,j):
            if(i<=-1 or i>=8 or j>=8 or j<=-1 or board[i][j]=="." or board[i][j]==color):
                return 0
            else:
                return 1
        if(check(rMove-1,cMove-1)):
            i=rMove-2
            j=cMove-2
            while(i>=0 and j>=0):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                i-=1
                j-=1
        if(check(rMove-1,cMove)):
            i=rMove-2
            j=cMove
            while(i>=0):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                i-=1
        if(check(rMove-1,cMove+1)):
            i=rMove-2
            j=cMove+2
            while(i>=0 and j<8):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                i-=1
                j+=1
        if(check(rMove,cMove-1)):
            i=rMove
            j=cMove-2
            while(j>=0):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                j-=1
        if(check(rMove,cMove+1)):
            i=rMove
            j=cMove+2
            while(j<8):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                j+=1
        if(check(rMove+1,cMove-1)):
            i=rMove+2
            j=cMove-2
            while(i<8 and j>=0):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                i+=1
                j-=1
        if(check(rMove+1,cMove)):
            i=rMove+2
            j=cMove
            while(i<8):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                i+=1
        if(check(rMove+1,cMove+1)):
            i=rMove+2
            j=cMove+2
            while(i<8 and j<8):
                if(board[i][j]==color):
                    return 1
                if(board[i][j]=="."):
                    break
                i+=1
                j+=1
        return 0