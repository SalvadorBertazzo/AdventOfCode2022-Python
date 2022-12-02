# ADVENT OF CODE 2022 - DAY-2
def first_task(opponent, me):
    picks = {"X": 1, "Y": 2, "Z": 3}
    count = picks.get(me)

    actions_A = {"X": 3, "Y": 6, "Z": 0}
    actions_B = {"X": 0, "Y": 3, "Z": 6}
    actions_C = {"X": 6, "Y": 0, "Z": 3}

    if opponent == "A":
        count += actions_A.get(me)
    elif opponent == "B":
        count += actions_B.get(me)
    elif opponent == "C":
        count += actions_C.get(me)
    return count


def second_task(opponent, me):
    picks = {"X": 0, "Y": 3, "Z": 6}
    count = picks.get(me)

    actions_A = {"X": 3, "Y": 1, "Z": 2}
    actions_B = {"X": 1, "Y": 2, "Z": 3}
    actions_C = {"X": 2, "Y": 3, "Z": 1}

    if opponent == "A":
        count += actions_A.get(me)
    elif opponent == "B":
        count += actions_B.get(me)
    elif opponent == "C":
        count += actions_C.get(me)
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
