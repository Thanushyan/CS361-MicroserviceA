import time

while True:
    # for i in range (1, 102):
    Value = input("Enter 'y' for yes, 'n' to quit: ").lower()
    
    if Value not in ["y", "n"]:
        print("Sorry that is an invalid input. Try again.")
        continue
    
    if Value == "n":
        with open("Food.txt", "w", encoding="utf-8") as file:
            file.write("")
            file.flush()
        break

    with open("Food.txt", "w", encoding="utf-8") as file:
        file.write("run")
        file.flush()
    time.sleep(4)    
    with open("Food.txt", "r", encoding="utf-8") as file:
        read = file.read()
        print(read)
    time.sleep(2)