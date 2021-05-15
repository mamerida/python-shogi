    if  a=="black":
        if int1== int3 and int2 != int4:
            if int4 > int2:
                for i in  range(int2+1,int4):
                    f = game_board2[int3][+i]
                    if f[-1] == "v":
                        print("you cant move for this box, you have other piece")
                        player_game.player_white().player_black_move()
                    elif f[-1] =="^":
                        player_game.player_black().captured_pieces_black.append(f)
                        moves(int1, int2 ,int3, i)
                        return None
                    else:
                        moves(int1, int2 ,int3, int4)
                        return None
            if int4 < int2:
                a = int2 - int4
                for i in  range(int4,int2-1):
                    f = game_board2[int3][+i]
                    if f[-1] == "v":
                        print("you cant move for this box, you have other piece")
                        player_game.playerblack().player_black_move()
                    elif f[-1] =="^":
                        j = i
                        moves(int1, int2 ,int3, j)
                        return None
                    else:
                        moves(int1, int2 ,int3, int4)
                        return None
        else:
            print("ilegal_move, pls repit")
            player_game.player_black().player_black_move()
