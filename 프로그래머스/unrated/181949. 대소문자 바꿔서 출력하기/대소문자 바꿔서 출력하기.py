s = ''
while True:
    s = input()
    
    if 1 <= len(s) <= 20:
        break

for i in range(len(s)):
    print(s[i].swapcase(), end="")
print()