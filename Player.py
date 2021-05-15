import moves

def player_black():
    def player_black_move(int1,int2,int3,int4):
        print("player Black ")
        int1= input("fila i ")
        int2= input("columna i ")
        int3= input("fila dest ")
        int4= input("columna dest  ")
        moves.player_move(int1,int2,int3,int4,0)
        return None
    player_black_move

def player_white():
    captured_pieces:[]
    def player_white_move():
        print("player White  ")
        int1= int(input("fila i  "))
        int2= int(input("columna i  "))
        int3= int(input("fila dest  "))
        int4= int(input("columna sdest  "))
        moves.player_move(int1,int2,int3,int4,0)
        return None
    player_white_move()
    player_black()
    return None
