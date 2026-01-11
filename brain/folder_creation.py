import os

print(os.getcwd())

for x in range(2,10):
    print(x)
    os.mkdir(f"./output/ver{x}")