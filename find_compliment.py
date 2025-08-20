def find_complementary(arr, target):
    index_number = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in index_number:
            return [index_number[complement], i]
        index_number[num] = i
    return []