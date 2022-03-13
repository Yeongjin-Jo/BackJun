import sys
N,X = map(int, sys.stdin.readline().split())
[print(i, end=" ") if int(i) < X else print("", end="") for i in sys.stdin.readline().split()]
