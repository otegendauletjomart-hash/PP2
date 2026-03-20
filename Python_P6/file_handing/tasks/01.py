import shutil
import os

f = open("sample.txt")
print(f.read())

with open("sample.txt", "a") as f:
    f.write("\nOh Hi")

shutil.copy("sample.txt", "sample_copy.txt")

file = "sample_copy.txt"

if os.path.exists(file):
    os.remove(file)
    print("Deleted")
else:
    print("File not found")