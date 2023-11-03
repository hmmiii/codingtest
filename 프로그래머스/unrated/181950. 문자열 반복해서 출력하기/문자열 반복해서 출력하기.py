while True:
    s, n = map(str, input().split())
    n = int(n)

    if 1 <= len(s) and len(s) <= 10 and 1 <= n <= 5 :
        break

n = int(n)

p = ''

for i in range(n):
    p += s;

print(p)