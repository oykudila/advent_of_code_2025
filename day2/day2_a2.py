import re


def main():
    helping_elves()


def helping_elves():
    duplicates = []

    file_path = "day2/input.txt"
    with open(file_path, "r") as file:
        lines = file.read().split(",")

    for line in lines:
        int_list = list(map(int, line.split("-")))
        id_ranges = list(range(int_list[0], int_list[1] + 1))
        str_ranges = list(map(str, id_ranges))
        for id in str_ranges:
            if re.match(r"^(\d+)\1+$", id):
                duplicates.append(id)

    duplicate_ints = list(map(int, duplicates))
    print("Answer 2:", sum(duplicate_ints))


if __name__ == "__main__":
    main()
