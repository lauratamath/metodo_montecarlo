from random import random, seed
import matplotlib.pyplot as plt

seed(12435687)

class GameSim():
  def __init__(self):
    self.houseProfit = 0
    self.playerPool = 0
    self.playerInitialMoney = 0
    self.gameProfits = []

  def game(self, moneyBet, bet): # Returns money earned and 0 otherwise
    token = round(random() * 100)
    if bet == 0: # Even number
      if token % 2 == 0 and token != 10:
        self.playerPool += moneyBet * 2
      elif token == 10:
        self.houseProfit += moneyBet
        self.playerPool -= moneyBet
      else:
        self.houseProfit += moneyBet
        self.playerPool -= moneyBet
    elif bet == 1: # Odd numbet
      if token == 11:
        self.houseProfit += moneyBet
        self.playerPool -= moneyBet
      elif token % 2 != 0:
        self.playerPool += moneyBet * 2
      else:
        self.houseProfit += moneyBet
        self.playerPool -= moneyBet

  def simulate(self, totalMoney, betPerGame, iterNumber, gameNumber):
    self.playerPool = totalMoney
    self.playerInitialMoney = totalMoney
    for i in range(iterNumber):
      for j in range(gameNumber):
        if self.playerPool > 0:
          choice  = round(random())
          self.playerPool -= betPerGame
          self.game(betPerGame, choice)
          self.gameProfits.append(self.playerPool)
        else:
          self.gameProfits.append(0)

    # plt.axhline(y=0.5, color='r', linestyle='-')
    plt.xlabel("Game")
    plt.ylabel('Player Money')
    plt.suptitle(f'50 juegos - Dinero inicial: {self.playerInitialMoney}')
    plt.plot(self.gameProfits)


sim = GameSim()

# Sim One
# sim.simulate(50000, 1000, 50, 10)

# Sim Two
# sim.simulate(50000, 1000, 50, 1000)

# Sim Three
# sim.simulate(100000, 10, 10000, 10)

# Test
sim.simulate(1000, 100, 10, 1)


plt.show()