# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

ans = 0
for i in range(H):
    for j in range(W):
        cnt = 0
        if S[i][j] == "#":
            cnt += 1
        if S[i-1][j] == "#":
            cnt += 1
        if S[i-1][j-1] == "#":
            cnt += 1
        if S[i][j-1] == "#":
            cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1

# answer
print("{}".format(ans))
