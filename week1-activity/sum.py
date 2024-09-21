def main():
    total = 0
    while True:
        user_input = input("Enter a number (or type 'stop' to end): ")
        if user_input.lower() == 'stop':
            break
        try:
            number = float(user_input)
            total += number
        except ValueError:
            print("Invalid input. Please enter a number.")
    print(f"The total sum is: {total}")

if __name__ == "__main__":
    main()