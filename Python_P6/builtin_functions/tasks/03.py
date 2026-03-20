name = ["Daulet", "Zhomart", "Zhanar"]

for i, name in enumerate(name):
    if name == "Zhomart":
        print("index:", i)

name = ["Daulet", "Zhomart", "Zhanar"]
scores = [175, 170, 168]

for name, score in zip(name, scores):
    if score < 170:
        print(name, "Shorter")