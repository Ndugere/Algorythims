def process_string(s: str) -> str:  # Renamed to avoid overriding built-in `input`
    if "$" in s:
        left, _ = s.split("$")  
        smallest_char = min(left) if left else None  
        removed = False  
        new_list = []  

        for i in s:
            if i == smallest_char and not removed:
                removed = True
                continue
            if i != "$":
                new_list.append(i)  

        return "".join(new_list)  # Convert list to string before returning

    mid_point = len(s) // 2  
    left = s[:mid_point]  
    smallest_char = min(left) if left else None  
    removed = False  
    new_list = []  

    for i in s:
        if i == smallest_char and not removed:
            removed = True
            continue
        new_list.append(i)  

    return "".join(new_list)  # Convert list to string before returning


def main():
    output = process_string("rttyhg$thththth")  # Updated function name
    print(output)  


if __name__ == "__main__":  
    main()  
