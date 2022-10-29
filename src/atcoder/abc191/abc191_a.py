# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
v, t, s, d = map(int, input().split())

# solve
ans = "Yes"
if t <= d/v and d/v <= s:
    ans = "No"

# answer
print("{}".format(ans))
