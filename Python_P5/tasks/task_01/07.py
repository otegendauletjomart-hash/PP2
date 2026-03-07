import re 

text = input()

pattern1 = re.sub(r"_\w", lambda a: a.group().upper(), text)
pattern2 = re.sub(r"_", "", pattern1)

print(pattern2)