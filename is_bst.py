#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

"""
def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
"""


class TreeOrders:
    """Binary tree traversals.
    Builds and outputs in-order, pre-order and post-order traversals of
    a rooted binary tree.
    Samples:
    """

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            self.key[i], self.left[i], self.right[i] = map(
                int, sys.stdin.readline().split()
            )
        return self.n

    def in_order(self):
        """In-order tree traversal."""
        current_id = 0
        stack = []

        while True:
            if current_id != -1:
                stack.append(current_id)
                current_id = self.left[current_id]
            elif stack:
                current_id = stack.pop()
                yield self.key[current_id]
                current_id = self.right[current_id]
            else:
                break



def main():
    tree = TreeOrders()
    number = tree.read()
    values = []
    tag = True

    if number != 0:

      for x in tree.in_order():
        values.append(x)

      for x in range(0, len(values)-1):
        m = values[x]
        n = values[x+1]
        if m >= n:
          print("INCORRECT")
          tag = False
          break

    if tag == True:
      print("CORRECT")



threading.Thread(target=main).start()
