import ast
def op(s: str) -> list:
    new_list = []
    s = ast.literal_eval(s)
    for a in s:
    
        if isinstance(a, str) and not a.isdigit() and a.isupper():
            new_list.append(a)
        
        elif isinstance(a, str) and not a.isdigit():
            for u in a:
                if u.isupper():
                    new_list.append(u)
    return new_list
def main():
    output = op('["RT", "Rt", 1, "2"]')
    print(output)
if __name__ == "__main__":
    main()