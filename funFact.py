import time
import random

stack = []

while True:
    with open("Food.txt", "r", encoding="utf-8") as file:
        read = file.read()
            
    if "run" in read:
        if len(stack) == 100:
            stack.clear()
        pr_num = random.randint(1, 100)
        while pr_num in stack:
            pr_num = random.randint(1, 100)
        stack.append(pr_num)
        with open("Food.txt", "w", encoding="utf-8") as file:
            file.write(str(pr_num))
            file.flush()
    time.sleep(2)