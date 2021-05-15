from pieces import Pown

class Board:

    def generate_board(self):
        rows = ["  "]
        board = []
        for j in range(0,9):
            board.append(rows*9)
        return board

    # put 9 white powns in the board "Pwv"
    def put_white_powns(self):
        board = self.generate_board()
        for i in range(9):
            board[2][i] = Pown()
        return board

    # put 9 black powns in the board "Pb^"
    def put_black_powns(self):
        board = self.put_white_powns()
        for i in range (9):
            board[6][i] = Pown()
        return board

    #put white king and black king in your box
    def put_kings(self):
        board = self.put_black_powns()
        board [0][4] = "Kv" # 0 4
        board [8][4] = "K^" # 8 4
        return board

    #put white and black hourse in the board
    def put_horse(self):
        board = self.put_kings()
        board[0][1] = "Hv" # 0 1
        board[0][7] = "Hv" # 0 7
        board[8][1] = "H^" # 8 1
        board[8][7] = "H^" # 8 7
        return board

    #put white and black lancers in the board lw v and "Lb ^"
    def put_lancer(self):
        board = self.put_horse()
        board[0][0] = "Lv" # 0 0
        board[0][8] = "Lv" # 0 8
        board[8][0] = "L^" # 8 0
        board[8][8] = "L^" # 8 8
        return board

    #put white and black gold general in the board
    def put_gold_general(self):
        board = self.put_lancer()
        board[0][3] = "Gv" # 0 3
        board[0][5] = "Gv"
        board[8][3] = "G^" # 8 3
        board[8][5] = "G^"
        return board

    #put white and black silver general  in the board
    def put_silver_general(self):
        board = self.put_gold_general()
        board[0][2] = "Sv" # 0 2
        board[0][6] = "Sv" #  06
        board[8][2] = "S^" # 8 2
        board[8][6] = "S^"
        return board

    def put_rook_and_bishop(self):
        board = self.put_silver_general()
        board[1][7] = "Rv" # 1 7
        board[1][1] = "Bv" # 1 1
        board[7][1] = "R^" # 7 1
        board[7][7] = "B^" # 7 7
        return board

    #generate the final board
    def generate_initial_board(self):
        board = self.put_rook_and_bishop()
        return board

    def show_board_status():
        board = self.generate_initial_board()
        print("       White Player v     ")
        print("  ============vv============")
        print(list(range(9)).join(" "))
        for i in range(9):
            print(list(range(9)),*board[i])
        print("  ============^^============")
        print("       Black Player ^     ")
