parts = input()


if len(parts) >= 2:  
    ok = True
    for part in parts.split("_"):
        if not part.islower() or not part.isalpha():
            ok = False
            break
    
    if ok:
        print("Yes")
    else:
        print("No")
else:
    print("No")