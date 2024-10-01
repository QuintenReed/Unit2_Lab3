from random import choice

class TicTacToe():

  def __init__(self):
    self.__board = [[" ", " ", " "] for i in range(3)]
    self.__turn = choice(["X", "O"])

  def __str__(self):
    text = ""
    for item in self.__board:
      text += " | ".join(item) + "\n"

    return text

  def __check_win(self, shape):
    win = False

    # I'm not sure if this was right
    if self.__board[0][0] == shape and self.__board[0][1] == shape and self.__board[0][2] == shape:
      win = True
    elif self.__board[0][0] == shape and self.__board[1][0] == shape and self.__board[2][0] == shape:
      win = True
    elif self.__board[0][0] == shape and self.__board[1][1] == shape and self.__board[2][2] == shape:
      win = True
    elif self.__board[0][2] == shape and self.__board[1][1] == shape and self.__board[2][0] == shape:
      win = True
    elif self.__board[1][0] == shape and self.__board[1][1] == shape and self.__board[1][2] == shape:
      win = True
    elif self.__board[2][0] == shape and self.__board[2][1] == shape and self.__board[2][2] == shape:
      win = True
    elif self.__board[0][1] == shape and self.__board[1][1] == shape and self.__board[2][1] == shape:
      win = True
    elif self.__board[0][2] == shape and self.__board[1][2] == shape and self.__board[2][2] == shape:
      win = True

    return win
  
  def place_token(self, row, column):
    if self.__board[row-1][column-1] == " ":
      self.__board[row-1][column-1] = self.__turn

      if self.__turn == "X":
        self.__turn = "O"
      elif self.__turn == "O":
        self.__turn = "X"

      return True
    else:
      return False
  
  def is_winner(self):
    x_win = self.__check_win("X")
    o_win = self.__check_win("O")

    winner = ""
    win = False

    if x_win == True:
      winner = "X"
      win = True
    elif o_win == True:
      winner = "O"
      win = True

    return win, winner