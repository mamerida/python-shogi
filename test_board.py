import unittest

from board import Board
from pieces import Pown

# #check are 2 white and  hourse in the board in your respective box
#     def test_quantity_hourse(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Hv")
#                  y = y + my_board.final_board()[i][j].count("H^")
#         self.assertEqual(2,y)
#         self.assertEqual(2,x)
#         self.assertEqual("Hv", my_board.final_board()[0][1])
#         self.assertEqual("Hv", my_board.final_board()[0][7])
#         self.assertEqual("H^", my_board.final_board()[8][1])
#         self.assertEqual("H^", my_board.final_board()[8][7])
# #check are 2 black lancers and 2 white lancers y respective box
#     def test_quantity_lancer(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Lv")
#                  y = y + my_board.final_board()[i][j].count("L^")
#         self.assertEqual(2,y)
#         self.assertEqual(2,x)
#         self.assertEqual("Lv", my_board.final_board()[0][0])
#         self.assertEqual("Lv", my_board.final_board()[0][8])
#         self.assertEqual("L^", my_board.final_board()[8][0])
#         self.assertEqual("L^", my_board.final_board()[8][8])
# #check are 2 black General Gol and 2 white General gol in your respective box
#     def test_quantity_gold_general(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Gv")
#                  y = y + my_board.final_board()[i][j].count("G^")
#         self.assertEqual(2,y)
#         self.assertEqual(2,x)
#         self.assertEqual("Gv", my_board.final_board()[0][3])
#         self.assertEqual("Gv", my_board.final_board()[0][5])
#         self.assertEqual("G^", my_board.final_board()[8][3])
#         self.assertEqual("G^", my_board.final_board()[8][5])
# #check are 2 black General SILVER and 2 white General SILVER in your respective box
#     def test_quantity_silver_general(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Sv")
#                  y = y + my_board.final_board()[i][j].count("S^")
#         self.assertEqual(2,y)
#         self.assertEqual(2,x)
#         self.assertEqual("Sv", my_board.final_board()[0][2])
#         self.assertEqual("Sv", my_board.final_board()[0][6])
#         self.assertEqual("S^", my_board.final_board()[8][2])
#         self.assertEqual("S^", my_board.final_board()[8][6])
# #check are 2 kings 1 white and 1 black in your respective box
#     def test_quantity_king(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Kv")
#                  y = y + my_board.final_board()[i][j].count("K^")
#         self.assertEqual(1,y)
#         self.assertEqual(1,x)
#         self.assertEqual("Kv", my_board.final_board()[0][4])
#         self.assertEqual("K^", my_board.final_board()[8][4])
# #check are 2 towers 1 white and 1 black in your respective box
#     def test_quantity_rook(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Rv")
#                  y = y + my_board.final_board()[i][j].count("R^")
#         self.assertEqual(1,y)
#         self.assertEqual(1,x)
#         self.assertEqual("Rv", my_board.final_board()[1][1])
#         self.assertEqual("R^", my_board.final_board()[7][1])
# #check are 2 bishop 1 white and 1 black in your respective box
#     def test_quantity_bishop(self):
#         x = 0
#         y = 0
#         for i in range(0,9):
#             for j in range(0,9):
#                  x = x + my_board.final_board()[i][j].count("Bv")
#                  y = y + my_board.final_board()[i][j].count("B^")
#         self.assertEqual(1,y)
#         self.assertEqual(1,x)
#         self.assertEqual("Bv", my_board.final_board()[1][7])
#         self.assertEqual("B^", my_board.final_board()[7][7])

class TestBoard(unittest.TestCase):

    # Check initial board has 9 rows
    def test_board_has_nine_rows(self):
        board = Board()
        self.assertEqual(len(board.generate_initial_board()), 9)

    # Check initial board has 9 white powns in the 2nd row = Pv
    def test_board_has_nine_pown_in_second_row(self):
        board = Board()
        for i in range(9):
            self.assertEqual(
                type(board.generate_initial_board()[2][i]),
                type(Pown())
            )

    # # Check bord has 9 black powns in the row 6 = P^
    def test_board_has_nine_pown_in_sixth_row(self):
        board = Board()
        for i in range(9):
            self.assertEqual(
                type(board.generate_initial_board()[6][i]),
                type(Pown())
            )
# #check are 2 white and  hourse in the board in your respective box
    def test_quantity_hourse(self):
        x = 0
        y = 0
        for i in range(0,9):
            for j in range(0,9):
                 x = x + my_board.final_board()[i][j].count("Hv")
                 y = y + my_board.final_board()[i][j].count("H^")
        self.assertEqual(2,y)
        self.assertEqual(2,x)
        self.assertEqual("Hv", my_board.final_board()[0][1])
        self.assertEqual("Hv", my_board.final_board()[0][7])
        self.assertEqual("H^", my_board.final_board()[8][1])
        self.assertEqual("H^", my_board.final_board()[8][7])
if __name__ == "__main__":
    unittest.main()
