s = input()

if s[0] == "a":
    ok = True
    
    for c in s[1:]:
        if c != "b":
            ok = False
            break
    
    if ok:
        print("Yes")
    else:
        print("No")
else:
    print("No")