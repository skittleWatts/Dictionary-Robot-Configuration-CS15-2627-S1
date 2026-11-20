robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

while True:
    print("""
-----------------------------------------
What would you like to do:
1. View all settings
2. Look up a setting
3. Change a setting
4. Add a setting
5. Exit the program

""")
    acceptable = ["1", "2", "3", "4", "5"]
    while True:
        user_input = input("Please enter your choice: ")
        if user_input in acceptable:
            int(user_input)
            break
        else:
            print("Please enter a valid input!")

    