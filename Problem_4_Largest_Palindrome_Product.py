"""
    Project Euler - Problem 4
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(number):
    return str(number) == str(number)[::-1]


def main():
    highest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            number = i * j
            if palindrome(number) and number > highest:
                highest = number

    print(highest)


if __name__ == "__main__":
    main()
