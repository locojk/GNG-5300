def main():
    try:
        # num1 is the dividend
        num1 = float(input("Enter the first number (dividend): "))
        # num2 is the divisor
        num2 = float(input("Enter the second number (divisor): "))
        
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of the division is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()