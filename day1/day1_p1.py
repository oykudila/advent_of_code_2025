def find_zeros(dial_pos, distance, direction):
    N = 100

    if direction == "R":
        offset = (-dial_pos) % N
        if offset == 0:
            offset = N
    else:
        offset = dial_pos % N
        if offset == 0:
            offset = N
    if distance < offset:
        return 0

    return 1 + (distance - offset) // N


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

        password += find_zeros(dial_pos, distance, direction)

        if direction == "R":
            dial_pos = (dial_pos + distance) % 100
        else:
            dial_pos = (dial_pos - distance) % 100
    return print("Final password:", password)


if __name__ == "__main__":
    dial()
