import os


for i in range(0, 2):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
