#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number"""
    last_digit = (number) % 5
    print(f"{last_digit}")
    return last_digit