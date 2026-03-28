import os

backup_file = "sample_backup.txt" 

if os.path.exists(backup_file):
    os.remove(backup_file)
    print(f"{backup_file} deleted successfully.")
else:
    print(f"{backup_file} does not exist.")