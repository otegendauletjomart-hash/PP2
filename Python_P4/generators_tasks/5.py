def gen5(n):
    for i in range(n, -1, -1):
        yield i

s = int(input())
print(', '.join(str(v) for v in gen5(s)))