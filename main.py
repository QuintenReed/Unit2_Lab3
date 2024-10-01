# Quinten Reed
# U2L3
# Tic-tac-toe

from tic_tac_toe import TicTacToe
from random import randint
from time import sleep

def rules():
  print("Tic-Tac-Toe")
  print("You draw an X or an O in any of the spots in the 3x3 grid, and if you get 3 in a row (either a straight line or a diagonal line) then you win.\n")

def position_input():
  # I have absolutely no idea how to word this
  pos2 = input("Which column will you play? (1-3) ")
  pos1 = input("Which row will you play? (1-3) ")

  try:
    pos1 = int(pos1)
    pos2 = int(pos2)

    if pos1 < 1 or pos1 > 3:
      print("Not a valid row")
      pos1 = False

    if pos2 < 1 or pos2 > 3:
      print("Not a valid column")
      pos2 = False
  except:
    print("Not a number")
    pos1 = False
    pos2 = False

  return pos1, pos2

def take_turn(G):
  pos1, pos2 = position_input()

  while pos1 == False or pos2 == False:
    pos1, pos2 = position_input()

  result = G.place_token(pos1, pos2)

  while result == False:
    print("Space is already taken")
    pos1, pos2 = position_input()

    while pos1 == False or pos2 == False:
      pos1, pos2 = position_input()

    result = G.place_token(pos1, pos2)

def bot_turn(G):
  bot_pos1 = randint(1, 3)
  bot_pos2 = randint(1, 3)
  result = G.place_token(bot_pos1, bot_pos2)

  while result == False:
    bot_pos1 = randint(1, 3)
    bot_pos2 = randint(1, 3)
    result = G.place_token(bot_pos1, bot_pos2)

def main():
  rules()
  G = TicTacToe()
  turn_num = 1
  win = False

  while turn_num < 5 and win == False:
    take_turn(G)
    print(G)
    win, winner = G.is_winner()

    if win == True:
      break

    print("The CPU is playing")
    sleep(1)
    bot_turn(G)
    print(G)
    win, winner = G.is_winner()
    turn_num += 1

  if win == False:
    print("No one won")
  else:
    print(f"{winner} wins!")

if __name__ == "__main__":
  main()