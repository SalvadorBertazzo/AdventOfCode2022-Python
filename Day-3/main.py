def split_line(line):
    arr = []
    arr[:0] = line
    arr.remove("\n")

    c1 = arr[:len(arr) // 2]
    c2 = arr[len(arr) // 2:]

    return c1, c2


def get_repeated(c1, c2):
    for elem in c1:
        if elem in c2:
            return elem


def find_number(repeated):
    lower_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                    'x': 24, 'y': 25, 'z': 26}
    upper_values = {}
    for k, v in lower_values.items():
        upper_values.update({k.upper(): v + 26})

    if repeated.islower():
        return lower_values.get(repeated)
    else:
        return upper_values.get(repeated)


def find_badge(a1, a2, a3):
    for i in a1:
        if i in a2 and i in a3:
            return i


def main():
    count = 0

    group = [[], [], []]
    group_size = 0
    count_badge = 0

    with open("input.txt") as file:
        for line in file:
            c1, c2 = split_line(line)
            repeated = get_repeated(c1, c2)
            count += find_number(repeated)

            group_size += 1
            if group_size <= 3:
                group[group_size-1] = c1 + c2
                if group_size == 3:
                    badge = find_badge(group[0], group[1], group[2])
                    count_badge += find_number(badge)
                    group_size = 0
                    group = [[], [], []]

        print("1st Result -> ", count)
        print("2nd Result -> ", count_badge)


if __name__ == '__main__':
    main()
