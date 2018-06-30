# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:

    def __init__(self):
        self.n = 0
        self.parent = []
        self.memo = [] # memoization

    def read(self):
        # Reads data.
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.memo = [0] * self.n # initialize to be zero, and then store true number

    def path_len(self, node_id):
        #Returns path length from given node to the root.
        parent = self.parent[node_id]
        if parent == -1:
            return 1

        if self.memo[node_id]: # if this node's height has been calculated, return it
            return self.memo[node_id]

        self.memo[node_id] = self.path_len(self.parent[node_id]) + 1
        return self.memo[node_id]

    def compute_height(self):
        #Choose the highest height of all nodes
        return max([self.path_len(i) for i in range(self.n)])


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
