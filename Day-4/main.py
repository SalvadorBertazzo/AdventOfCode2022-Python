def get_pair(line):
    first_elve, second_elve = "", ""
    pair = line.split(",")

    first = True
    for i in pair:
        if first:
            first_elve = i
            first = False
        else:
            second_elve = i

    return tuple(map(int, first_elve.split('-'))), tuple(map(int, second_elve.split('-')))


def check_pair_full(first, second):
    return (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1])


def check_pair_overlap(first, second):
    return not (first[1] < second[0] or second[1] < first[0])


def main():
    count_full = 0
    count_overlap = 0

    with open("input.txt") as file:
        for line in file:
            first_elve, second_elve = get_pair(line)

            if check_pair_full(first_elve, second_elve):
                count_full += 1
            if check_pair_overlap(first_elve, second_elve):
                count_overlap += 1

    print("Fully contains count -> ", count_full)
    print("Overlaps count -> ", count_overlap)


if __name__ == '__main__':
    main()
