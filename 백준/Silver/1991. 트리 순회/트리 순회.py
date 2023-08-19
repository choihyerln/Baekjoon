import sys
input = sys.stdin.readline

n = int(input().strip())
tree = {}

for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def preorder(root):     # 루트 -> 왼 -> 오 탐색
    if root != '.':
        print(root, end="")         # root
        preorder(tree[root][0])     # left -> left가 새로운 root가 된다.
        preorder(tree[root][1])     # right-> right가 새로운 root가 된다.
    
def inorder(root):      # 왼 -> 루트 -> 오른 탐색
    if root != '.':
        inorder(tree[root][0])      # left
        print(root, end='')         # root
        inorder(tree[root][1])      # right

def postorder(root):
    if root != '.':
        postorder(tree[root][0])    # left
        postorder(tree[root][1])    # right
        print(root, end='')         # root

preorder('A')
print()
inorder('A')
print()
postorder('A')