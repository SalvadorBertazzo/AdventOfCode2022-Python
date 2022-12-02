# ADVENT OF CODE 2022 - DAY-2
def first():
    score = 0

    with open("input.txt") as file:
        for line in file:
            splitted = line.split(" ")
            opponent = splitted[0]
            me = splitted[1].rsplit()[0]

            # -Your pick-
            # Rock
            if me == "X":
                score += 1
            # Paper
            elif me == "Y":
                score += 2
            # Scissors
            elif me == "Z":
                score += 3

            # -Opponents pick-
            # Rock
            if opponent == "A":
                # -Your pick-
                # Rock
                if me == "X":
                    score += 3
                # Paper
                elif me == "Y":
                    score += 6
                # Scissors
                elif me == "Z":
                    score += 0
            # Paper
            elif opponent == "B":
                # -Your pick-
                # Rock
                if me == "X":
                    score += 0
                # Paper
                elif me == "Y":
                    score += 3
                # Scissors
                elif me == "Z":
                    score += 6
            # Scissors
            elif opponent == "C":
                # -Your pick-
                # Rock
                if me == "X":
                    score += 6
                # Paper
                elif me == "Y":
                    score += 0
                # Scissors
                elif me == "Z":
                    score += 3

        print("-First score: ", score)


def second():
    score = 0

    with open("input.txt") as file:
        for line in file:
            splitted = line.split(" ")
            opponent = splitted[0]
            me = splitted[1].rsplit()[0]

            # Rock
            if opponent == "A":
                if me == "X":
                    score += 0 + 3
                elif me == "Y":
                    score += 3 + 1
                elif me == "Z":
                    score += 6 + 2
            # Paper
            elif opponent == "B":
                if me == "X":
                    score += 0 + 1
                elif me == "Y":
                    score += 3 + 2
                elif me == "Z":
                    score += 6 + 3
            # Scissors
            elif opponent == "C":
                if me == "X":
                    score += 0 + 2
                elif me == "Y":
                    score += 3 + 3
                elif me == "Z":
                    score += 6 + 1

        print("-Second score: ", score)


if __name__ == '__main__':
    first()
    second()
