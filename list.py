def input(s: list) -> list:
    new_list = []
    for a in s:
        if isinstance(a, int):
            new_list.append(a)
        elif isinstance(a, str) and a.isdigit():
            new_list.append(int(a))
    return new_list

def main():
    output = input(['rrrt', '23', 14, 'dog'])
    print(output)

if __name__ == "__main__":
    main()
