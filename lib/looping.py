#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown in range (10, 0, -1):
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [i**2 for i in int_list]


def get_result(num): 
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: 
        return num


def fizzbuzz():
    for i in range(1,101):
        print(get_result(i))

