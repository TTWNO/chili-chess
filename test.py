import threading
import berserk
import chess
from berserk.enums import GameType

my_board = chess.Board()

class myThread (threading.Thread):
   def __init__(self, threadID, func):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.func = func
   def run(self):
      self.func()

session = berserk.TokenSession("Ikuclhu7r4iGmO2B")
client = berserk.Client(session=session)

game = client.challenges.create_ai(variant=GameType.CRAZYHOUSE)
print(game)
ie = client.board.stream_game_state(game["id"])

def print_info():
  for x in ie:
    if x["type"] == "gameState":
      uci = x["moves"].split(" ")[-1]
      move = my_board.push_uci(uci)
      print(move)
      print(x)
    else:
      print(x)

def user_input():
  while True:
    i = input()
    try:
      res = client.board.make_move(game["id"], i)
      print(res)
    except:
      print("ERROR!")

t = myThread(1, user_input)
t2 = myThread(2, print_info)

t1.start()
t2.start()
