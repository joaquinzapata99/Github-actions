def add(x, y):
    return x + y


def calculator():
    print("Simple Addition Calculator")
    print("Enter 'q' at any time to quit")

    while True:
        try:
            first_input = input("\nEnter first number: ")
            if first_input.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break

            second_input = input("Enter second number: ")
            if second_input.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break

            num1 = float(first_input)
            num2 = float(second_input)

            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
