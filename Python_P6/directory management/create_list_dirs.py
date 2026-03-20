import os

# Create nested directories
os.makedirs("test_dir/subdir1/subdir2", exist_ok=True)

# List files and folders
path = "test_dir"

print("All files and directories:")
for item in os.listdir(path):
    print(item)

# List only directories
print("\nDirectories only:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

# Find files by extension
print("\nFind .txt files:")
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))