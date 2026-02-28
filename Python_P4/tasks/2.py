s = input()

if len(s) in (3, 4) and s[0] == "a":
    if s[1:] == "b" * (len(s) - 1):
        print("Yes")
    else:
        print("No")
else:
    print("No")