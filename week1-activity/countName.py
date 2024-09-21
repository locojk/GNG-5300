def count_characters(name):
    char_count = {}
    for char in name:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == "__main__":
    name = input("Enter a name: ")
    result = count_characters(name)
    print("Character count:", result)

