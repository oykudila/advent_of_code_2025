from itertools import combinations


def main():
    finding_twelves()


def finding_twelves():
    file_path = "day3/input.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        batteries = []
        for line in lines:
            banks = list(str(line).strip())
            coms = list(combinations(banks, 12))
            print(coms)
            # TODO find all combinations of 12 digits in the line
       
            # coms = combinations(lines, 12)
        # print(coms)


if __name__ == "__main__":
    main()
