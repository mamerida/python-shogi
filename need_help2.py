white_prisoner = []
black_prisoner = []
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
capture_piece("Hcv")
capture_piece("Bv")
print(black_prisoner)
capture_piece("S^")
capture_piece("Bc^")
print(white_prisoner)



game_board2[int3][int4] = game_board2[int1][int2]
game_board2[int1][int2] = "  "
board_shogi(game_board2)


            f = moves.game_board2[recentFF][recentCF]
            if  recentFF == 8 and f == "Pv" or f == "Lv":
                if f == "Pv":
                    moves.game_board2[recentFF][recentCF] = "Pcv"
                    player_black()
                if f == "Lv":
                    moves.game_board2[recentFF][recentCF] = "Lcv"
                    player_black()
            elif  recentFF == 7 and f == "Hv":
                moves.game_board2[recentFF][recentCF] = "Hcv"
                player_black()
            elif f =="Kv" or f == "Gv":
                player_black()
            elif recentFI == 6 or recentFI == 7 or recentFI == 8 or recentFF == 6 or recentFF == 7 or recentFF == 8:
                print("desea promocionar la pieza que acaba de mover? Coloque 1 si es asi")
                int1=int(print("coloque 0 o 1"))
                if int1 == 1:
                    f = f[0]
                    f = f + "cv"
                    moves.game_board2[recentFF][recentCF] = f
                else:
                    player_black()
            else:
                player_black()
