def main():
    dial()
    print("Done")


def dial():
    dial_pos = 50
    password = 0

    file_path = "day1/input.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

    print("Dialing...")
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "R":
            dial_pos = (dial_pos + distance) % 100
            # print(f"New dial position: {dial_pos}")
        elif direction == "L":
            dial_pos = (dial_pos - distance) % 100
            # print(f"New dial position: {dial_pos}")
        if dial_pos == 0:
            password += 1
            print(f"Dial hit 0! Current password count: {password}")

    print(f"Password is: {password}")


if __name__ == "__main__":
    main()
