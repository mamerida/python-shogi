class generate_board():
    def generate_board():
        rows = [" "]
        board = []
        for j in range(0,9):
            board.append(rows*9)
        return board
# put 9 white powns in the board "Pwv"
    def put_pieces():
        board = generate_board()
        def put_white_powns():
            print("hola")
            for i in range (9):
                board[2][i] = "Pw v"
                return board
        put_white_powns()
        return board
# put 9 black powns in the board "Pb^"
