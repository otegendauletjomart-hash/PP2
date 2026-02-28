def gen3(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

s = int(input())
for v in gen3(s):
    print(v)