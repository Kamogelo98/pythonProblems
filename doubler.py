""" doubler(numbers) method that takes an array of numbers and returns a new array
where every element of the original array is multiplied by 2"""


def doubler(numbers):
    numbers = [1, 2, 3, 4]
    new_arr = []
    for x in numbers:
        new_arr.append(x*2)

    print(new_arr)


doubler([5, 6, 7, 8])
