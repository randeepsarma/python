import os


# os.rename(f"ffvvgvyvyv.jpg", f"one.jpg")

files = os.listdir()
i = 0
for file in files:
    if file == "main.py":
        continue
    os.rename(f"{file}", f"{i}.jpg")
    i += 1
    print(file)
