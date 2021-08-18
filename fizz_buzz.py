def fizz_buzz(max):
    max = int(input("Enter maximum number: "))
    x = 0
    nums = []

    while(x < max):

        if x % 4 == 0 or x % 6 == 0:
            if not (x % 4 == 0 and x % 6 == 0):

                nums.append(x)
        x += 1
    print(nums)


fizz_buzz(100)
