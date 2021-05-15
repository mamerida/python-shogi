import moves

black_prisoner = []
white_prisoner = []
recentWmoves = []
recentFI = 0
recentCI = 0
recentFF = 0
recentCF = 0
BrecentFI = 0
BrecentCI = 0
BrecentFF = 0
BrecentCF = 0
def test_numbers(int1,int2,int3,int4):
    control = False
    a =[0,1,2,3,4,5,6,7,8]
    b = a.count(int1)
    c = a.count(int2)
    d = a.count(int3)
    e = a.count(int3)
    if b == 1 and c == 1 and d == 1 and e == 1:
        control = True
    return control

def recentmoves(FI,CI,FD,CD,f):
    if f[-1] == "v":
        recentWmoves.insert(0,FI)
        recentWmoves.insert(1,CI)
        recentWmoves.insert(2,FD)
        recentWmoves.insert(3,CD)
    else:
        BrecentFI = FI
        BrecentCI = CI
        BrecentFF= FD
        BrecentCF = CD
    return recentFI,recentFF,recentCI,recentCF
def player_black():
    def player_black_put_piece():
        xcontrola  =0
        a = [ ]
        acontrol = None
        print("pls coloque la fila y la columna donde desea ingresar la pieza")
        int1= int(input("fila   "))
        int2= int(input("columna   "))
        int3= int(input("number of piece in the list, pls start with zero  "))
        g = black_prisoner[int3]
        f = moves.game_board2[int1][int2]
        if f !="  ":
            print("you can't place this piece there,there is another piece in that place ")
            player_black()
        else:
            if g == "L^" and int1 == 8:
                print("you cant place this piece there, pls try again, ")
                player_black()
            elif g == "H^" and int1 == 7 or int1 == 8:
                print("you cant place this piece there, pls try again. ")
                player_black()
            elif g == "P^" and int== 8 :
                print("you cant place this piece there, pls try again ")
                player_black()
            else:
                if g == "P^":
                    for i in range(0,8):
                        a.append(moves.game_board2[i][int2])
                    print(a)
                    if a.count("P^") != 0:
                        print("you cant place this piece there, you have another pawn in the same row ")
                        player_black()
                    else:
                        moves.game_board2[int1][int2] = g
                        black_prisoner.remove(g)
                        rpieceFilaB = int1
                        rpieceColumnaB= int2
                        moves.board_shogi(moves.game_board2)
                        player_white()
                moves.game_board2[int1][int2] = g
                black_prisoner.remove(g)
                rpieceFilaB = int1
                rpieceColumnaB= int2
                moves.board_shogi(moves.game_board2)
                player_white()

        return None
    def player_black_move():
        print("player Black ")
        int1= int(input("fila i  "))
        int2= int(input("columna i  "))
        int3= int(input("fila dest  "))
        int4= int(input("columna sdest  "))
        control = False
        control = test_numbers(int1,int2,int3,int4)
        if control == True:
            moves.player_move(int1,int2,int3,int4,"black")
            f = moves.game_board2[recentWmoves[2]][recentWmoves[3]]
            if  recentWmoves[2] == 0 and f == "P^" or f == "L^":
                if f == "P^":
                    moves.game_board2[recentWmoves[2]][recentWmoves[3]] = "Pc^"
                    moves.board_shogi(moves.game_board2)
                    player_white()
                if f == "L^":
                    moves.game_board2[recentWmoves[2]][recentWmoves[3]] = "Lc^"
                    moves.board_shogi(moves.game_board2)
                    player_white()
            elif  recentFF == 1 and f == "H^":
                moves.game_board2[recentWmoves[2]][recentWmoves[3]] = "Hc^"
                moves.board_shogi(moves.game_board2)
                player_white()
            elif f =="K^" or f == "G^":
                player_white()
            #elif recentFI == 6 or recentFI == 7 or recentFI == 8 or recentFF == 6 or recentFF == 7 or recentFF == 8:
            elif recentWmoves[0] == 0 or recentWmoves[0] == 1 or recentWmoves[0] == 2 or recentWmoves[2] == 0 or recentWmoves[2] == 1 or recentWmoves[2] == 2:
                print("desea promocionar la pieza que acaba de mover? Coloque 1 si es asi")
                control=int(input("coloque 0 o 1"))
                if control == 1:
                    f = f[0]
                    f = f + "c^"
                    moves.game_board2[recentWmoves[2]][recentWmoves[3]] = f
                    moves.board_shogi(moves.game_board2)
                    player_white()
                else:
                    player_white()
        else:
            print("invalid imput, pls try again")
            player_black_move()
        return None
    if len(black_prisoner)!= 0:
        print("Do you want to place a piece on board? coloque 1 si es asi si no ponga 0")
        int1 = int(input("coloque 0 o 1 "))
        if int1 == 1:
            player_black_put_piece()
        else:
            player_black_move()
    else:
        player_black_move()
    return None



def player_white():
    def player_white_put_piece():
        xcontrola  =0
        a = [ ]
        acontrol = None
        print("pls coloque la fila y la columna donde desea ingresar la pieza")
        int1= int(input("fila   "))
        int2= int(input("columna   "))
        int3= int(input("number of piece in the list, pls start with zero  "))
        g = white_prisoner[int3]
        f = moves.game_board2[int1][int2]
        if f !="  ":
            print("you can't place this piece there,there is another piece in that place ")
            player_white()
        else:
            if g == "Lv" and int1 == 8:
                print("you cant place this piece there, pls try again, ")
                player_white()
            elif g == "Hv" and int1 == 7 or int1 == 8:
                print("you cant place this piece there, pls try again. ")
                player_white()
            elif g == "Pv" and int== 8 :
                print("you cant place this piece there, pls try again ")
                player_white()
            else:
                if g == "Pv":
                    for i in range(0,8):
                        a.append(moves.game_board2[i][int2])
                    print(a)
                    if a.count("Pv") != 0:
                        print("you cant place this piece there, you have another pawn in the same row ")
                        player_white()
                    else:
                        moves.game_board2[int1][int2] = g
                        white_prisoner.remove(g)
                        rpieceFila = int1
                        rpieceColumna= int2
                        moves.board_shogi(moves.game_board2)
                        player_black()
                moves.game_board2[int1][int2] = g
                white_prisoner.remove(g)
                rpieceFila = int1
                rpieceColumna= int2
                moves.board_shogi(moves.game_board2)
                player_black()

        return None
    def player_white_move():
        print("player White move ")
        int1= int(input("fila i  "))
        int2= int(input("columna i  "))
        int3= int(input("fila dest  "))
        int4= int(input("columna sdest  "))
        control = False
        control = test_numbers(int1,int2,int3,int4)
        if control == True:
            moves.player_move(int1,int2,int3,int4,"white")
            f = moves.game_board2[recentWmoves[2]][recentWmoves[3]]
            if  recentWmoves[2] == 8 and f == "Pv" or f == "Lv":
                if f == "Pv":
                    moves.game_board2[recentWmoves[2]][recentWmoves[3]] = "Pcv"
                    moves.board_shogi(moves.game_board2)
                    player_black()
                if f == "Lv":
                    moves.game_board2[recentWmoves[2]][recentWmoves[3]] = "Lcv"
                    moves.board_shogi(moves.game_board2)
                    player_black()
            elif  recentFF == 7 and f == "Hv":
                moves.game_board2[recentWmoves[2]][recentWmoves[3]] = "Hcv"
                moves.board_shogi(moves.game_board2)
                player_black()
            elif f =="Kv" or f == "Gv":
                player_black()
            #elif recentFI == 6 or recentFI == 7 or recentFI == 8 or recentFF == 6 or recentFF == 7 or recentFF == 8:
            elif recentWmoves[0] == 6 or recentWmoves[0] == 7 or recentWmoves[0] == 8 or recentWmoves[2] == 6 or recentWmoves[2] == 7 or recentWmoves[2] == 8:
                print("desea promocionar la pieza que acaba de mover? Coloque 1 si es asi")
                control=int(input("coloque 0 o 1"))
                if control == 1:
                    f = f[0]
                    f = f + "cv"
                    moves.game_board2[recentWmoves[2]][recentWmoves[3]] = f
                    moves.board_shogi(moves.game_board2)
                    player_black()
                else:
                    player_black()
        else:
            print("invalid imput, pls try again")
            player_white()
        return None

    if len(white_prisoner)!= 0:
        print("Do you want to place a piece on board? coloque 1 si es asi si no ponga 0")
        int1 = int(input("coloque 0 o 1 "))
        if int1 == 1:
            player_white_put_piece()
        else:
            player_white_move()
    else:
        player_white_move()
    return None
def capture_piece(f):
    if f[-1]=="v":
        f = f[0:-1]
        if f[-1]=="c":
            f = f[0:-1]
            f= f + "^"
            black_prisoner.append(f)
        else:
            f= f + "^"
            black_prisoner.append(f)
    elif f[-1] =="^":
        f = f[0:-1]
        if f[-1]=="c":
            f = f[0:-1]
            f= f + "v"
            white_prisoner.append(f)
        else:
            f= f + "v"
            white_prisoner.append(f)
    elif f =="Kv":
        print("CONGRATULATIONS player black win")
    elif f =="K^":
        print("CONGRATULATIONS player white win")
    return white_prisoner, black_prisoner
