# This code implement a data structure to store a set of integers and quickly compute range sums.
# Task. Implement a data structure that stores a set 𝑆 of integers with the following allowed operations:
# ∙ insert(𝑖) — add integer 𝑖 into the set 𝑆 (if it was there already, the set doesn’t change).
# ∙ erase(𝑖) — remove integer 𝑖 from the set 𝑆 (if there was no such element, nothing happens).
# ∙ search(𝑖) — check whether 𝑖 is in the set 𝑆 or not.
# ∙ sum(𝑙, 𝑟) — output the sum of all elements 𝑣 in 𝑆 such that 𝑙 ≤ 𝑣 ≤ 𝑟.

### EXAMPLE
# Input:
# 15
# ? 1
# + 1
# ? 1
# + 2
# s 1 2
# + 1000000000
# ? 1000000000
# - 1000000000
# ? 1000000000
# s 999999999 1000000000
# - 2
# ? 2
# - 0
# + 9
# s 0 9
# Output:
# Not found
# Found
# 3
# Found
# Not found
# 1
# Not found
# 10

# python3

from sys import stdin

# Splay tree implementation
# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v) #need two update to make sure the tree is right updated
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)

# Makes splay of the given vertex and makes it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key): #make sure find the smallest bigger number
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)

def split(root, key):
    (result, root) = find(root, key)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

def merge(left, right): # the left is smaller than all elements in right (assumption)
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

# Code that uses splay tree to solve the problem
root = None
# add integer into the set
def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)

# remove integer from the set    
def erase(x):
    global root
    # find the x
    (left, right) = split(root, x)
    # check wheter x is in the tree
    if right == None or right.key != x:
        root = merge(left, right)
        return
    else:
        root = merge(left, right.right)
        if root != None:
            root.parent = None

# check whether interger is in the set
def search(x):
    global root
    # find the key
    (result, root) = find(root, x)
    if root == None or root.key != x:
        return False
    else:
        return True

# output the sum of all element in S which is in the range between fr and to
def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    if middle != None:
        ans = middle.sum
    else:
        ans = 0
    # Complete the implementation of sum
    root = merge(left, merge(middle, right))
    return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
