def remove(smallest_char, s):
    removed= False
    new_list = []
    for i in s:
        if i == smallest_char and removed != True:
            removed = True
            continue
        if i != "$":
            new_list.append(i)
    return "".join(new_list)

def input(s: str) -> str:
    if "$" in s:
        left, _ = s.split("$")
        smallest_char = min(left) if left else None
        return remove(smallest_char, s)
        
    mid_point = int(len(s) // 2)
    smallest_char = s[ :mid_point]
    remove(smallest_char, s)
    
    
    

def main():
    output = input("arrrrrrrtfffffff$")
    print(output)

if __name__ == "__main__":
    main()