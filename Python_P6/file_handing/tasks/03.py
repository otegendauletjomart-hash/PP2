with open("sample.txt", "a") as f: 
    f.write("Konichiwa\n")
    f.write("Salem\n")

with open("sample.txt", "r") as f:
    print("Updated file contents:\n", f.read())