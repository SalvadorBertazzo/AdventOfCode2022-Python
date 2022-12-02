# ADVENT OF CODE 2022 - DAY-2
def first_task(opponent, me):
    count = 0
    # -Your pick-
    # Rock
    if me == "X":
        count += 1
    # Paper
    elif me == "Y":
        count += 2
    # Scissors
    elif me == "Z":
        count += 3

    # -Opponents pick-
    # Rock
    if opponent == "A":
        # -Your pick-
        # Rock
        if me == "X":
            count += 3
        # Paper
        elif me == "Y":
            count += 6
        # Scissors
        elif me == "Z":
            count += 0
    # Paper
    elif opponent == "B":
        # -Your pick-
        # Rock
        if me == "X":
            count += 0
        # Paper
        elif me == "Y":
            count += 3
        # Scissors
        elif me == "Z":
            count += 6
    # Scissors
    elif opponent == "C":
        # -Your pick-
        # Rock
        if me == "X":
            count += 6
        # Paper
        elif me == "Y":
            count += 0
        # Scissors
        elif me == "Z":
            count += 3

    return count


def second_task(opponent, me):
    count = 0
    # Rock
    if opponent == "A":
        if me == "X":
            count += 0 + 3
        elif me == "Y":
            count += 3 + 1
        elif me == "Z":
            count += 6 + 2
    # Paper
    elif opponent == "B":
        if me == "X":
            count += 0 + 1
        elif me == "Y":
            count += 3 + 2
        elif me == "Z":
            count += 6 + 3
    # Scissors
    elif opponent == "C":
        if me == "X":
            count += 0 + 2
        elif me == "Y":
            count += 3 + 3
        elif me == "Z":
            count += 6 + 1

    return count


def main():
    first_score = 0
    second_score = 0

    with open("input.txt") as file:
        for line in file:
            splitted_line = line.split(" ")
            opponent = splitted_line[0]
            me = splitted_line[1].rsplit()[0]

            first_score += first_task(opponent, me)
            second_score += second_task(opponent, me)

    print("-RESULTS-")
    print("1st Task -> ", first_score)
    print("2nd Task -> ", second_score)


if __name__ == '__main__':
    main()
