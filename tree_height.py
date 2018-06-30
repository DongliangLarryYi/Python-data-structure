# Implement the tree data structure, store the tree and compute its height.
"""
Task: You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
Input Format: The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.
Output Format: Output the height of the tree.

Sample 1.
Input:
5
4 -1 4 1 1
Output:
3
Explanation:
The input means that there are 5 nodes with numbers from 0 to 4, node 0 is a child of node 4, node 1
is the root, node 2 is a child of node 4, node 3 is a child of node 1 and node 4 is a child of node 1. To
see this, let us write numbers of nodes from 0 to 4 in one line and the numbers given in the input in
the second line underneath:
0 1 2 3 4
4 -1 4 1 1
Now we can see that the node number 1 is the root, because −1 corresponds to it in the second line.
Also, we know that the nodes number 3 and number 4 are children of the root node 1. Also, we know
that the nodes number 0 and number 2 are children of the node 4.
"""
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
