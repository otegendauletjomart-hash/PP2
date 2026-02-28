s = input()

if s[0].isupper():
    ok = True
    
    for c in s[1:]:
        if c.isupper():
            ok = False
            break
    
    if ok:
        print("Yes")
    else:
        print("No")
else:
    print("No")