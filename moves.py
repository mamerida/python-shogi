import my_board
import player_game
import itertools
#to retorn the board
game_board2= my_board.final_board()
def board_shogi(b):
    board = b
    guide = [0,1,2,3,4,5,6,7,8]
    print("       White Player v     ")
    print("white capture pieces ",player_game.white_prisoner)
    print("  ============vv============")
    print(" ", *guide , sep="  ")
    for i in range(9):
        print(guide[i],*board[i])
    print("  ============^^============")
    print("black capture pieces ",player_game.black_prisoner)
    print("       Black Player ^     ")



# define the basic moves
def moves(int1, int2 ,int3, int4):
    f = game_board2[int1][int2]
    game_board2[int3][int4] = game_board2[int1][int2]
    game_board2[int1][int2] = "  "
    player_game.recentmoves(int1,int2,int3,int4,f)
    board_shogi(game_board2)



#define condition of moves of diferent pieces
def powns(int1, int2 ,int3, int4,a):
    if  a=="white":
        if int1+1 == int3 and int2 == int4:
            f = game_board2[int3][int4]
            if f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            elif f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int4)

                return None
            else:
                moves(int1, int2 ,int3, int4)

                return None
        else:
            print("ilegal_move, pls repit")
            player_game.player_white().player_white_move()
    elif  a=="black":
        if int1-1 == int3 and int2== int4:
            f = game_board2[int3][int4]
            if f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            elif f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int4)

            else:
                moves(int1, int2 ,int3, int4)

        else:
            print("ilegal_move, pls repit")
            player_game.player_black().player_black_move()
def hourse(int1, int2 ,int3, int4,a):
    if  a=="white":
        if int1+2 == int3:
            if  int2-1 == int4 or int2+1 == int4:
                f = game_board2[int3][int4]
                if f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)

                    return None
                else:
                    moves(int1, int2 ,int3, int4)

                    return None
        else:
            print("ilegal_move, pls repit")
            player_game.player_white().player_white_move()
    elif  a=="black":
        if int1-2 == int3:
            if int2-1 == int4 or int2+1 == int4:
                f = game_board2[int3][int4]
                if f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1, int2 ,int3, int4)

        else:
            print("ilegal_move, pls repit")
            player_game.player_black().player_black_move()
    return game_board2
def rook(int1, int2 ,int3, int4,a):
    if  a=="white":
        if int1 < int3 and int2 == int4:
            a = []
            f= None
            i=0
            for i in range(int1+1,int3):
                a.append(game_board2[i][int2])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1+i, int4)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
        elif int1 > int3 and int2 == int4:#check
            a=[]
            f = None
            i =0
            for i in range(int3,int1):
                a.insert(0,game_board2[i][int2])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1-i, int4)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2< int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int2+1,int4+1):
                a.append(game_board2[int1][i])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2+i)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2>int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int4,int2):
                a.insert(0,game_board2[int3][i])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2-i)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        else:
            print("ilegal move, pls repit")
            player_game.player_white().player_white_move()
    if  a=="black":
        if int1 < int3 and int2 == int4:
            a = []
            f= None
            i=0
            for i in range(int1+1,int3):
                a.append(game_board2[i][int2])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1+i, int4)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black()
            else:
                moves(int1, int2 ,int3, int4)
        elif int1 > int3 and int2 == int4:#check
            a=[]
            f = None
            i =0
            for i in range(int3,int1):
                a.insert(0,game_board2[i][int2])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1-i, int4)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2< int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int2+1,int4+1):
                a.append(game_board2[int1][i])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2+i)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2>int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int4,int2):
                a.insert(0,game_board2[int3][i])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2-i)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        else:
            print("ilegal move, pls repit")
            player_game.player_black().player_black_move()
    return None
def bishop(int1,int2,int3,int4,a):
    if a =="white":
        if int3 > int1 and int4>int2:
            if int3 -int1 == int4 -int2:
                a =[]
                f = None
                x = int1-int2
                for j,i in itertools.product(range(int2+1,int4+1),range(int1+1,int3+1)):
                    if i-j == x :
                            a.append(game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1+i+1, int2+i+1)
                elif f[-1] == "v":
                   print("you cant move for this box, you have other piece")
                   player_game.player_white().player_white_move()
                else:
                    moves(int1, int2 ,int3, int4)
                return None
            else:
                print("ilegal move, pls repit")
                player_game.player_white().player_white_move()
        elif int3 > int1 and int4< int2:
            if int3 - int1 ==  int2 - int4:
                a =[]
                f = None
                x = int1+int2
                for j,i in itertools.product(range(int4,int2),range(int1+1,int3+1)):
                    if i+j ==x:
                        a.insert(0,game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1+i+1, int2-i-1)
                elif f[-1] == "v":
                   print("you cant move for this box, you have other piece")
                   player_game.player_white().player_white_move()
                else:
                    moves(int1, int2 ,int3, int4)
            else:
                print("ilegal move, pls repit")
                player_game.player_white().player_white_move() # no anda
        elif int3 < int1 and int4>int2:
            if int2+int1 == int4+int3:
                a =[]
                q = 0
                f = None
                x = int1+int2
                for j,i in itertools.product(range(int2-1,int4+1),range(int3-1,int1)):
                    if j+i== x:
                        a.append(game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1-1-i, int2+1+i)
                elif f[-1] == "v":
                   print("you cant move for this box, you have other piece")
                   player_game.player_white().player_white_move()
                else:
                    moves(int1, int2 ,int3, int4)
            else:
                print("ilegal move, pls repit")
                player_game.player_white().player_white_move()
        elif int3 < int1 and int4 < int2:
            if int1-int2 ==  int3 - int4:
                a =[]
                f = None
                q = 0
                x = int1-int2
                for j,i in itertools.product(range(int4,int2),range(int3,int1)):
                    if i-j==x:
                        a.insert(0,game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    q = q +1
                    if f[-1] == "^" or f[-1] == "v":
                        break
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1-i-1, int2-i-1)
                elif f[-1] == "v":
                   print("you cant move for this box, you have other piece")
                   player_game.player_white().player_white_move()
                else:
                    moves(int1, int2 ,int3, int4)
        else:
            print("ilegal move, pls repit")
            player_game.player_white().player_white_move()


    if a == "black":
        if int3 > int1 and int4>int2:
            if int3 -int1 == int4 -int2:
                a =[]
                f = None
                x = int1-int2
                for j,i in itertools.product(range(int2+1,int4+1),range(int1+1,int3+1)):
                    if i-j == x :
                            a.append(game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1+i+1, int2+i+1)
                elif f[-1] == "^":
                   print("you cant move for this box, you have other piece")
                   player_game.player_black().player_black_move()
                else:
                    moves(int1, int2 ,int3, int4)
            else:
                print("ilegal move, pls repit")
                player_game.player_black().player_black_move()
        if int3 > int1 and int4< int2:
            if int3 - int1 ==  int2 - int4:
                a =[]
                f = None
                x = int1+int2
                for j,i in itertools.product(range(int4,int2),range(int1+1,int3+1)):
                    if i+j ==x:
                        a.insert(0,game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1+i+1, int2-i-1)
                elif f[-1] == "^":
                   print("you cant move for this box, you have other piece")
                   player_game.player_black().player_black_move()
                else:
                    moves(int1, int2 ,int3, int4)
            else:
                print("ilegal move, pls repit")
                player_game.player_black().player_black_move()
        if int3 < int1 and int4>int2:
            if int2+int1 == int4+int3:
                a =[]
                q = 0
                f = None
                x = int1+int2
                for j,i in itertools.product(range(int2-1,int4+1),range(int3-1,int1)):
                    if j+i== x:
                        a.append(game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1-1-i, int2+1+i)
                elif f[-1] == "^":
                   print("you cant move for this box, you have other piece")
                   player_game.player_black().player_black_move()
                else:
                    moves(int1, int2 ,int3, int4)
            else:
                print("ilegal move, pls repit")
                player_game.player_black().player_black_move()
        if int3 < int1 and int4 < int2:
            if int1-int2 ==  int3 - int4:
                a =[]
                f = None
                q = 0
                x = int1-int2
                for j,i in itertools.product(range(int4,int2),range(int3,int1)):
                    if i-j==x:
                        a.insert(0,game_board2[i][j])
                for i in range(0,len(a)):
                    f=a[i]
                    q = q +1
                    if f[-1] == "^" or f[-1] == "v":
                        break
                for i in range(0,len(a)):
                    f=a[i]
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1-i-1, int2-i-1)
                elif f[-1] == "^":
                   print("you cant move for this box, you have other piece")
                   player_game.player_black().player_black_move()
                else:
                    moves(int1, int2 ,int3, int4)
            else:
                print("ilegal move, pls repit")
                player_game.player_black().player_black_move()
def lancer(int1, int2 ,int3, int4,a):
    if a =="white":
        if int1 < int3 and int2 == int4:
                a = []
                f= None
                i=0
                for i in range(int1+1,int3+1):
                    a.append(game_board2[i][int2])
                for i in range(0,len(a)):
                    f=a[i]
                    i = i + 1
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1+i, int4)
                elif f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                else:
                    moves(int1, int2 ,int3, int4)

        else:
            print("ilegal move, pls repit")
            player_game.player_white().player_white_move()

    elif a == "black":
        if int1 > int3 and int2 == int4:
                a = []
                f= None
                i=0
                for i in range(int3,int1):
                    a.insert(0,game_board2[i][int2])
                for i in range(0,len(a)):
                    f=a[i]
                    i = i + 1
                    if f[-1] == "^" or f[-1] == "v":
                        break
                if f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int1-i+1, int4)
                elif f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                else:
                    moves(int1, int2 ,int3, int4)

        else:
            print("ilegal move, pls repit")
            player_game.player_black().player_black_move()

    return None
#def bishop(int1, int2 ,int3, int4,a):
    if a == "white":
        if int3 > int1 and int4> int2:
            if int3 - int1 == int4 - int2:
                a = []
                f= None
                i=0
                for i in range(int1+1,int3+1):
                    for j in range(int2+1,int4+1):

                        a.append(game_board2[i][int2])
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
                return None
        elif int3 < int1 and int4> int2:
            if int1 - int3 == int4 -int2:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        elif int3 < int1 and int4 < int2:
            if int1 - int3 == int2 -int4:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        elif int3 > int1 and int4 > int2:
            if int1 - int3 == int2 -int4:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        else:
            print("ilegal_move, pls repit")
            player_game.player_white().player_white_move()
    if a == "black":
        if int3 > int1 and int4> int2:
            if int3 - int1 == int4 - int2:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
                return None
        elif int3 < int1 and int4> int2:
            if int1 - int3 == int4 -int2:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        elif int3 < int1 and int4 < int2:
            if int1 - int3 == int2 -int4:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        elif int3 > int1 and int4 > int2:
            if int1 - int3 == int2 -int4:
                return None
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        else:
            print("ilegal_move, pls repit")
            player_game.player_black().player_black_move()
def king(int1, int2 ,int3, int4,a):
    if a == "white":
        if int1 == int3:
            if int2 == int4 +1 or int2 == int4 -1 :
                f = game_board2 [int3][int4]
                if f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        elif int1+1 == int3:
            if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        elif int1-1 == int3:
            if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] =="v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
        else:
            print("ilegal_move, pls repit")
            player_game.player_white().player_white_move()
    if a == "black":
        if int1 == int3:
            if int2 == int4 +1 or int2 == int4 -1 :
                f = game_board2 [int3][int4]
                if f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        elif int1+1 == int3:
            if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        elif int1-1 == int3:
            if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] =="^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
        else:
            print("ilegal_move, pls repit")
            player_game.player_black().player_black_move()
    return None
def gold_general(int1, int2 ,int3, int4,a):
    if a == "white":
        if int1 == int3:
            if int2 == int4 +1 or int2 == int4 -1 :
                f = game_board2 [int3][int4]
                if f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        elif int1+1 == int3:
            if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        elif int1-1 == int3:
            if int2 == int4:
                f =game_board2[int3][int4]
                if f[-1] =="v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_white().player_white_move()
        else:
            print("ilegal_move, pls repit")
            player_game.player_white().player_white_move()
    if a == "black":
        if int1 == int3:
            if int2 == int4 +1 or int2 == int4 -1 :
                f = game_board2 [int3][int4]
                if f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        elif int1-1 == int3:
            if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        elif int1+1 == int3:
            if int2 == int4:
                f =game_board2[int3][int4]
                if f[-1] =="^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
            else:
                print("ilegal_move, pls repit")
                player_game.player_black().player_black_move()
        else:
            print("ilegal_move, pls repit")
            player_game.player_black().player_black_move()
    return None
def silver_general(int1, int2 ,int3, int4,a):
        if a == "white":
            if int1+1 == int3:
                if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] == "v":
                        print("you cant move for this box, you have other piece")
                        player_game.player_white().player_white_move()
                    elif f[-1] =="^":
                        player_game.capture_piece(f)
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_white().player_white_move()
            elif int1-1 == int3:
                if int2-1 == int4 or int2+1 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] =="v":
                        print("you cant move for this box, you have other piece")
                        player_game.player_white().player_white_move()
                    elif f[-1] =="^":
                        player_game.capture_piece(f)
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_white().player_white_move()
            else:
                print("ilegal move, pls repit")
                player_game.player_white().player_white_move()
        if a == "black":
            if int1-1 == int3:
                if int2 == int4 or int2+1 == int4 or int2-1 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] == "^":
                        print("you cant move for this box, you have other piece")
                        player_game.player_black().player_black_move()
                    elif f[-1] =="v":
                        player_game.capture_piece(f)
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal move, pls repit")
                    player_game.player_black_move().player_black_move()
            elif int1+1 == int3:
                if int2-1 == int4 or int2+1 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] =="^":
                        print("you cant move for this box, you have other piece")
                        player_game.player_black().player_black_move()
                    elif f[-1] =="^":
                        player_game.capture_piece(f)
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_black().player_black_move()
            else:
                print("ilegal move, pls repit")
                player_game.player_black().player_black_move()
def crowned_rook(int1, int2 ,int3, int4,a):
    if  a=="white":
        if int1 < int3 and int2 == int4:
            a = []
            f= None
            i=0
            for i in range(int1+1,int3):
                a.append(game_board2[i][int2])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1+i, int4)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
        elif int1 > int3 and int2 == int4:#check
            a=[]
            f = None
            i =0
            for i in range(int3,int1):
                a.insert(0,game_board2[i][int2])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1-i, int4)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2< int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int2+1,int4+1):
                a.append(game_board2[int1][i])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2+i)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2>int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int4,int2):
                a.insert(0,game_board2[int3][i])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="^":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2-i)
            elif f[-1] == "v":
                print("you cant move for this box, you have other piece")
                player_game.player_white().player_white_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int1+1 == int3:
            if  int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] == "v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
        elif int1-1 == int3:
            if  int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] =="v":
                    print("you cant move for this box, you have other piece")
                    player_game.player_white().player_white_move()
                elif f[-1] =="^":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
        else:
            print("ilegal move, pls repit")
            player_game.player_white().player_white_move()
    if  a=="black":
        if int1 < int3 and int2 == int4:
            a = []
            f= None
            i=0
            for i in range(int1+1,int3):
                a.append(game_board2[i][int2])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1+i, int4)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black()
            else:
                moves(int1, int2 ,int3, int4)
        elif int1 > int3 and int2 == int4:#check
            a=[]
            f = None
            i =0
            for i in range(int3,int1):
                a.insert(0,game_board2[i][int2])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int1-i, int4)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2< int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int2+1,int4+1):
                a.append(game_board2[int1][i])

            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2+i)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int2>int4 and int1 == int3:#check
            a = []
            f= None
            i=0
            for i in range(int4,int2):
                a.insert(0,game_board2[int3][i])
            for i in range(0,len(a)):
                f=a[i]
                i = i + 1
                if f[-1] == "^" or f[-1] == "v":
                    break
            if f[-1] =="v":
                player_game.capture_piece(f)
                moves(int1, int2 ,int3, int2-i)
            elif f[-1] == "^":
                print("you cant move for this box, you have other piece")
                player_game.player_black().player_black_move()
            else:
                moves(int1, int2 ,int3, int4)
            return None
        elif int1+1 == int3:
            if  int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] == "^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
        elif int1-1 == int3:
            if  int2+1 == int4 or int2-1 == int4:
                f =game_board2[int3][int4]
                if f[-1] =="^":
                    print("you cant move for this box, you have other piece")
                    player_game.player_black().player_black_move()
                elif f[-1] =="v":
                    player_game.capture_piece(f)
                    moves(int1, int2 ,int3, int4)
                else:
                    moves(int1,int2,int3,int4)
        else:
            print("ilegal move, pls repit")
            player_game.player_black().player_black_move()
    return None
def crowned_bishop(int1, int2 ,int3, int4,a):
        if a =="white":
            if int3 > int1 and int4>int2:
                if int3 -int1 == int4 -int2:
                    a =[]
                    f = None
                    x = int1-int2
                    for j,i in itertools.product(range(int2+1,int4+1),range(int1+1,int3+1)):
                        if i-j == x :
                                a.append(game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="^":
                        moves(int1, int2 ,int1+i+1, int2+i+1)
                    elif f[-1] == "v":
                       print("you cant move for this box, you have other piece")
                       player_game.player_white().player_white_move()
                    else:
                        moves(int1, int2 ,int3, int4)
            if int3 > int1 and int4< int2:
                if int3 - int1 ==  int2 - int4:
                    a =[]
                    f = None
                    x = int1+int2
                    for j,i in itertools.product(range(int4,int2),range(int1+1,int3+1)):
                        if i+j ==x:
                            a.insert(0,game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="^":
                        moves(int1, int2 ,int1+i+1, int2-i-1)
                    elif f[-1] == "v":
                       print("you cant move for this box, you have other piece")
                       player_game.player_white().player_white_move()
                    else:
                        moves(int1, int2 ,int3, int4)
                else:
                    print("ilegal move, pls repit")
                    player_game.player_white().player_white_move() # no anda
            if int3 < int1 and int4>int2:
                if int2+int1 == int4+int3:
                    a =[]
                    q = 0
                    f = None
                    x = int1+int2
                    for j,i in itertools.product(range(int2-1,int4+1),range(int3-1,int1)):
                        if j+i== x:
                            a.append(game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="^":
                        moves(int1, int2 ,int1-1-i, int2+1+i)
                    elif f[-1] == "v":
                       print("you cant move for this box, you have other piece")
                       player_game.player_white().player_white_move()
                    else:
                        moves(int1, int2 ,int3, int4)
            if int3 < int1 and int4 < int2:
                if int1-int2 ==  int3 - int4:
                    a =[]
                    f = None
                    q = 0
                    x = int1-int2
                    for j,i in itertools.product(range(int4,int2),range(int3,int2)):
                        if i-j==x:
                            a.insert(0,game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        q = q +1
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="^":
                        moves(int1, int2 ,int1-i-1, int2-i-1)
                    elif f[-1] == "v":
                       print("you cant move for this box, you have other piece")
                       player_game.player_white().player_white_move()
                    else:
                        moves(int1, int2 ,int3, int4)
            if int1+1 == int3:
                if int2 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] == "v":
                        print("you cant move for this box, you have other piece")
                        player_game.player_white().player_white_move()
                    elif f[-1] =="^":
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_white().player_white_move()
            if int1-1 == int3:
                if int2 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] =="v":
                        print("you cant move for this box, you have other piece")
                        player_game.player_white().player_white_move()
                    elif f[-1] =="^":
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_white().player_white_move()
            if int1 == int3:
                if int2 == int4 +1 or int2 == int4 -1 :
                    f = game_board2 [int3][int4]
                    if f[-1] == "v":
                        print("you cant move for this box, you have other piece")
                        player_game.player_white().player_white_move()
                    elif f[-1] =="^":
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_white().player_white_move()
            else:
                print("ilegal move, pls repit")
                player_game.player_white().player_white_move()


        if a == "black":
            if int3 > int1 and int4>int2:
                if int3 -int1 == int4 -int2:
                    a =[]
                    f = None
                    x = int1-int2
                    for j,i in itertools.product(range(int2+1,int4+1),range(int1+1,int3+1)):
                        if i-j == x :
                                a.append(game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="v":
                        moves(int1, int2 ,int1+i+1, int2+i+1)
                    elif f[-1] == "^":
                       print("you cant move for this box, you have other piece")
                       player_game.player_black().player_black_move()
                    else:
                        moves(int1, int2 ,int3, int4)
            if int3 > int1 and int4< int2:
                if int3 - int1 ==  int2 - int4:
                    a =[]
                    f = None
                    x = int1+int2
                    for j,i in itertools.product(range(int4,int2),range(int1+1,int3+1)):
                        if i+j ==x:
                            a.insert(0,game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="v":
                        moves(int1, int2 ,int1+i+1, int2-i-1)
                    elif f[-1] == "^":
                       print("you cant move for this box, you have other piece")
                       player_game.player_black().player_black_move()
                    else:
                        moves(int1, int2 ,int3, int4)
                else:
                    print("ilegal move, pls repit")
                    player_game.player_white().player_white_move() # no anda
            if int3 < int1 and int4>int2:
                if int2+int1 == int4+int3:
                    a =[]
                    q = 0
                    f = None
                    x = int1+int2
                    for j,i in itertools.product(range(int2-1,int4+1),range(int3-1,int1)):
                        if j+i== x:
                            a.append(game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="v":
                        moves(int1, int2 ,int1-1-i, int2+1+i)
                    elif f[-1] == "^":
                       print("you cant move for this box, you have other piece")
                       player_game.player_black().player_black_move()
                    else:
                        moves(int1, int2 ,int3, int4)
            if int3 < int1 and int4 < int2:
                if int1-int2 ==  int3 - int4:
                    a =[]
                    f = None
                    q = 0
                    x = int1-int2
                    for j,i in itertools.product(range(int4,int2),range(int3,int2)):
                        if i-j==x:
                            a.insert(0,game_board2[i][j])
                    for i in range(0,len(a)):
                        f=a[i]
                        q = q +1
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    for i in range(0,len(a)):
                        f=a[i]
                        if f[-1] == "^" or f[-1] == "v":
                            break
                    if f[-1] =="v":
                        moves(int1, int2 ,int1-i-1, int2-i-1)
                    elif f[-1] == "^":
                       print("you cant move for this box, you have other piece")
                       player_game.player_black().player_black_move()
                    else:
                        moves(int1, int2 ,int3, int4)
            if int1+1 == int3:
                if int2 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] == "^":
                        print("you cant move for this box, you have other piece")
                        player_game.player_black().player_black_move()
                    elif f[-1] =="v":
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_white().player_white_move()
            if int1-1 == int3:
                if int2 == int4:
                    f =game_board2[int3][int4]
                    if f[-1] =="^":
                        print("you cant move for this box, you have other piece")
                        player_game.player_black().player_black_move()
                    elif f[-1] =="v":
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_black().player_black_move()
            if int1 == int3:
                if int2 == int4 +1 or int2 == int4 -1 :
                    f = game_board2 [int3][int4]
                    if f[-1] == "^":
                        print("you cant move for this box, you have other piece")
                        player_game.player_black().player_black_move()
                    elif f[-1] =="v":
                        moves(int1, int2 ,int3, int4)
                    else:
                        moves(int1,int2,int3,int4)
                else:
                    print("ilegal_move, pls repit")
                    player_game.player_black().player_black_move()
            else:
                print("ilegal move, pls repit")
                player_game.player_black().player_black_move()

def player_move(int1,int2,int3,int4,b):
    a = game_board2[int1][int2]
    if b =="white" and a == "  ":
        print("you dont have peace in this position pls try again ")
        player_game.player_white().player_white_move()
    elif b =="white" and a[-1] == "^":
        print("you cant move this peace pls try again")
        player_game.player_white().player_white_move()
    elif b =="black" and a[-1] == "v":
        print("you cant move this peace pls try again")
        player_game.player_black().player_black_move()
    elif b =="black" and a =="  ":
        print("you dont have peace in this position pls try again ")
        player_game.player_black().player_black_move()
    elif b == "white" and a[-1] == "v":
        if a == "Pv" or a =="Pkv":
            powns(int1,int2,int3,int4,b)
        elif a =="Hv" or a =="Hkv" :
            hourse(int1, int2 ,int3, int4,b)
        elif a == "Sv" or a =="Skv":
            silver_general(int1, int2 ,int3, int4,b)
        elif a == "Gv" or a == "Gkv"  or a == "Pcv" or a == "Hcv" or a == "Lcv" or a == "Scv" :
            gold_general(int1, int2 ,int3, int4,b)
        elif a == "Kv":
            king(int1, int2 ,int3, int4,b)
        elif a == "Lv":
            lancer(int1, int2 ,int3, int4,b)
        elif a == "Bv":
            bishop(int1, int2 ,int3, int4,b)
        elif a == "Rv":
            rook(int1, int2 ,int3, int4,b)
        elif a == "Rcv":
            crowned_rook(int1, int2 ,int3, int4,b)
        elif a == "Bcv":
            crowned_rook(int1, int2 ,int3, int4,b)
    elif b == "black" and a[-1] == "^":
        if a == "P^" or a =="Pk^":
            powns(int1,int2,int3,int4,b)
        elif a =="H^" or a =="Hk^" :
            hourse(int1, int2 ,int3, int4,b)
        elif a == "S^" or a =="Sk^":
            silver_general(int1, int2 ,int3, int4,b)
        elif a == "G^" or a == "Gk^"  or a == "Pc^" or a == "Hc^" or a == "Lc^" or a == "Sc^" :
            gold_general(int1, int2 ,int3, int4,b)
        elif a == "K^":
            king(int1, int2 ,int3, int4,b)
        elif a == "L^":
            lancer(int1, int2 ,int3, int4,b)
        elif a == "B^":
            bishop(int1, int2 ,int3, int4,b)
        elif a == "R^":
            rook(int1, int2 ,int3, int4,b)
        elif a == "Rc^":
            crowned_rook(int1, int2 ,int3, int4,b)
        elif a == "Bc^":
            crowned_rook(int1, int2 ,int3, int4,b)
