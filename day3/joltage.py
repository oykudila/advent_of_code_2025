def main():
    finding_banks()


def find_first_digit(banks):
    curr_max = max(banks)
    f_index = banks.index(curr_max)
    if f_index == 99:
        edge_banks = banks[:-1]
        return find_first_digit(edge_banks)
    else:
        return curr_max, f_index


def finding_banks():
    file_path = "day3/input.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        batteries = []
        for line in lines:

            banks = list(str(line).strip())

            first_digit, f_index = find_first_digit(banks)
            second_digit = max(banks[f_index + 1 :])

            batteries.append(first_digit + second_digit)

        print(sum(list(map(int, batteries))))


if __name__ == "__main__":
    main()
