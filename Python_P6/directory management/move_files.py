import shutil
import os

# Ensure directories exist
os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# Create a sample file
with open("source/sample.txt", "w") as f:
    f.write("Hello!")

# Copy file
shutil.copy("source/sample.txt", "destination/sample_copy.txt")

# Move file
shutil.move("source/sample.txt", "destination/sample_moved.txt")

print("Files copied and moved successfully")