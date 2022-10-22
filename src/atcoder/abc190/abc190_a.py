# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a, b, c = map(int, input().split())

# solve
if a > b or c == 1 and a == b:
    ans = "Takahashi"
else:
    ans = "Aoki"

# answer
print("{}".format(ans))
