s = 0
ss = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
    s = s + c
    ss += c
print(s)
print(ss)


print(sum(x for x in range(1,500) if x % 2 != 0 and x % 3 == 0))
