def input(s: str):
    new_list = []
    for a in s:
        
        if a not in ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]:
            continue
        new_list.append(a)

    return "".join(new_list)
        
def main():
    output = input("1w0010wertes4")
    print(output)

if __name__ == "__main__":
    main()