import shutil

shutil.copy(
    "project/data/input/file1.txt",
    "project/data/output/file1_copy.txt"
)

shutil.move(
    "project/data/input/file2.txt",
    "project/data/output/file2_moved.txt"
)