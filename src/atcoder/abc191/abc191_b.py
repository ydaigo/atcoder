# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N, X = map(int, input().split())
A = list(map(str, input().split()))

# solve
ans = ""
for i in range(len(A)-1, -1, -1):
    if A[i] == str(X):
        A.pop(i)
if len(A) != 0:
    ans = " ".join(A)

# answer
print("{}".format(ans))
