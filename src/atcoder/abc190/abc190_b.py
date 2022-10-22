# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N, S, D = map(int, input().split())

ans = "No"
for i in range(N):
    X, Y = map(int, input().split())
    if X < S and Y > D:
        ans = "Yes"

# answer
print("{}".format(ans))
