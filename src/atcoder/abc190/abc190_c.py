# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for i in range(K)]

ans = 0
for i in range(1 << K):
    dish = [0] * N
    for j in range(K):
        if (i >> j) & 1:
            dish[CD[j][0]-1] += 1
        else:
            dish[CD[j][1]-1] += 1
    sum_i = 0
    for k in range(M):
        if dish[AB[k][0]-1] > 0 and dish[AB[k][1]-1] > 0:
            sum_i += 1
    if ans < sum_i:
        ans = sum_i

# answer
print("{}".format(ans))
