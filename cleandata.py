def input(s: str) -> str:
    if "$" in s:
        left, _ = s.split("$")
        smallest_char = min(left) if left else None
        removed = False
        new_list = []
        for i in s:
            if i == smallest_char and removed != True:
                removed = True
                continue
            if i != "$":
                new_list.append(i)
        return new_list
    mid_point = int(len(s)// 2)
    left = s[ :mid_point]
    smallest_char = min(left) if left else None
    removed = False
    new_list = []
    for i in s:
        if i == smallest_char and removed != True:
            removed = True
            continue
        new_list.append(i)
    return new_list


def main():
    output = input("rttyhg$thththth")
    print(output)

if __name__ == "__main__":
    main()