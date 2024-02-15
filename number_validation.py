# Arundhathi B
# Python program for validating a number.

def validate_number(min_num, max_num, disabled_numbers, num):
        
            if num < min_num or num > max_num:
                print("Invalid input.")
                return
            
            if num not in disabled_numbers:
                print("Validated number:", num)
            
            else:
                print(num, "is disabled number.")
                num += 1
                return validate_number(min_num, max_num, disabled_numbers, num)

def main():
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    
    disabled_numbers = set(map(int, input("Enter the disabled numbers separated by space: ").split()))
    num = int(input("Enter a number to validate: "))

    validate_number(min_num, max_num, disabled_numbers, num)


if __name__ == "__main__":
    main()
