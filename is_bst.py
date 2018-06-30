# Problem: Is it a binary search tree?
"""
Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛− 1 in order. Each of these lines contains
three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.
Output Format. If the given binary tree is a correct binary search tree (see the definition in the problem
description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes).

Sample 1.
Input:
3
2 1 2
1 -1 -1
3 -1 -1
Output:
CORRECT
"""
#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
    # read and store tree data
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
