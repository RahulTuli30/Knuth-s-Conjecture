from collections import namedtuple
from collections import defaultdict


class BFS():
    __slots__ = "init", "goal", "actions", "parents"

    default = namedtuple("default", "parent")(None)
    IterationLimit = 1000
    error_message = "Not Found or Iteration limit reached"

    def __init__(self, init, goal, actions):
        assert init is not None, "No initial state provided"
        assert goal is not None, "No goal state provided"
        assert actions, "There must be at-least one action to modify state"

        self.init = init
        self.goal = goal
        self.actions = actions
        self.parents = defaultdict(lambda: BFS.default)

    def start(self, verbose=False):
        queue = [self.init]
        self.parents = defaultdict(lambda: BFS.default)
        self.parents[self.init] = None
        completed = False
        iteration = 0
        while not completed:
            state = queue.pop(0)
            if verbose:
                print("At state {}".format(state))
            if self.is_goal(state):
                return self.make_path(state, verbose)

            for action in self.actions:
                successor = action(state)
                if successor is not None:
                    if self.parents[successor] == BFS.default:
                        self.parents[successor] = state
                        queue.append(successor)

            iteration += 1
            completed = len(queue) == 0 or iteration == BFS.IterationLimit

        return BFS.error_message

    def is_goal(self, state):
        return state == self.goal

    def make_path(self, state, verbose=False):
        if verbose:
            print("Congrats! found the goal, returning the path")

        path = []
        while self.parents[state]:
            if verbose:
                print(state)
            path.append(state)
            state = self.parents[state]

        path.append(self.init)
        return list(reversed(path))

    @staticmethod
    def set_iteration_limit(limit, verbose=False):
        BFS.IterationLimit = limit
        if verbose:
            print("Successfully set the new Iteration limit to {}".format(
                BFS.IterationLimit))
        return BFS.IterationLimit
