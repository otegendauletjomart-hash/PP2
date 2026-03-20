import os 

with open("project/data/input/file1.txt", "w") as f:
    f.write("Hello 1")

with open("project/data/input/file2.txt", "w") as f:
    f.write("Hello 2")

with open("project/data/input/file3.log", "w") as f:
    f.write("Log file")

path = "project/data"

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    
    if os.path.isdir(full_path):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")
