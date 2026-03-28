import shutil

backup_file = "sample_backup.txt"
shutil.copy("sample.txt", backup_file) 
print(f"{"sample.txt"} copied to {backup_file}")