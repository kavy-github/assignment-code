num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0 and num % 10 != 0:
    print("The number is divisible by both 3 and 5 but not by 10.")
else:
    print("The number does not meet the condition.")
