def gen2(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

s = int(input())
print(', '.join(str(v) for v in gen2(s)))