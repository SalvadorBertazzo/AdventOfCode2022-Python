# ADVENT OF CODE 2022 - DAY-1
def main():
    dic = {}
    i = 0
    dic[i] = 0
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                i += 1
                dic[i] = 0
                continue
            else:
                dic[i] = dic[i] + int(line)
    sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(sort_dic[0][1]+sort_dic[1][1]+sort_dic[2][1])


if __name__ == '__main__':
    main()
