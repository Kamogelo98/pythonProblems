def average_of_three(num1, num2, num3):
    num1 = int(input("Please enter number 1: "))
    num2 = int(input("Please enter number 2: "))
    num3 = int(input("Please enter number 3: "))

    sum = num1 + num2 + num3

    average = sum//3
    print("The average is : ", average)


average_of_three(5, 10, 15)
