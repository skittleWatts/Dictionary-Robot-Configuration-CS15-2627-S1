robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print(f"The name of the robot is {robot["name"]}.")
print(f"The model of the robot is {robot["model"]}.")

robot["battery"] = 100

robot["colour"] = "red"

robot.pop("mode")

print(f"The robot has a total of {len(robot)} attributes.")

print("This is everything we know about the robot:")

for key, value in robot.items():
    print(f"{key}: {value}")