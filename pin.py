from time import sleep

for i in range(0000, 10000):
    print(f"checkling {i:04}")
    sleep(.1)

with open ("large", "r") as file:
    for word in file.readlines():
        print(f"Checking {word.rstrip()}...")
        sleep(.1)
       
