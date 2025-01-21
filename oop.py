class Data:
    def __init__(self, s):
        self.s = s

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, s):
        if "$" in s:
            left, _ = s.split("$", 1)  
            min_char = min(left) if left else None
        else:
            mid_point = len(s) // 2
            left = s[:mid_point]
            min_char = min(left) if left else None

       
        removed = False
        new_list = []
        for i in s:
            if i == min_char and not removed:
                removed = True
                continue
            if i != "$":
                new_list.append(i)

        
        self._s = "".join(new_list)

    def __str__(self):
        return self.s


def main():
    s = Data("rty$rrr")
    print(s)


if __name__ == "__main__":
    main()
