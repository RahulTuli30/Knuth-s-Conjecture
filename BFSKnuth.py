from BFS import *
from Knuth import *

def search(init, goal):
    algo = BFS(init, goal, KnuthActions)
    print(algo.start(verbose=True))

if __name__ == '__main__':
    print("Let's play with Knuth's Conjecture")
    init = int(input("Initial State(Should be greater than or equal to 3):"))
    goal = int(input("Goal State(Any positive Integer number):"))
    search(init, goal)