def gameboard(board):
    print("Game Board State : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(board[i]==0):
            print("- ",end=" ");
        if (board[i]==1):
            print("O ",end=" ");
        if(board[i]==-1):    
            print("X ",end=" ");
    print("\n\n");

def gamerTurn(board):
    position=input("Enter X's position from [1-9]: ");
    position=int(position);
    if(board[position-1]!=0):
        print("Wrong Move!!");
        exit(0) ;
    board[position-1]=-1;

def minimax(board,player):
    z=assort(board);
    if(z!=0):
        return (z*player);
    position = -1;
    val = -2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            points=-minimax(board,(player*-1));
            if(points>val):
                val=points;
                position=i;
            board[i]=0;

    if(position==-1):
        return 0;
    return val;

def AITurn(board):
    position=-1;
    val=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            points=-minimax(board, -1);
            board[i]=0;
            if(points>val):
                val=points;
                position=i;
 
    board[position]=1;

def assort(board):
    currentb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(board[currentb[i][0]] != 0 and
           board[currentb[i][0]] == board[currentb[i][1]] and
           board[currentb[i][0]] == board[currentb[i][2]]):
            return board[currentb[i][2]];
    return 0;

def main():
    board=[0,0,0,0,0,0,0,0,0];
    print("Computer : O Vs. Player : X");
    player= input("Enter to play 1(st) or 2(nd) : ");
    player = int(player);
    for i in range (0,9):
            if(assort(board)!=0):
                break;
            if((i+player)%2==0):
                AITurn(board);
            else:
                gameboard(board);
                gamerTurn(board);

    z=assort(board);
    if(z==0):
         gameboard(board);
         print("The Game Is Draw!!")
    if(z==-1):
         gameboard(board);
         print("Player Wins!!")
    if(z==1):
         gameboard(board);
         print("AI Wins!!")
       
main()