# Number Analyzer Project
# Beginner-friendly implementation


def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return original == reverse


def reverse_integer(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n

    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return sign * reverse


def is_power_of_two(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    return n == 1


def is_ugly(n):
    if n <= 0:
        return False

    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor

    return n == 1


def is_happy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False

        seen.add(n)
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return True


def count_primes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1

    count = 0
    for i in range(n):
        if is_prime[i]:
            count += 1

    return count


def main():
    print("NUMBER ANALYZER")
    print("1. Palindrome Number")
    print("2. Reverse Integer")
    print("3. Power of Two")
    print("4. Ugly Number")
    print("5. Happy Number")
    print("6. Count Primes")

    choice = int(input("Enter your choice: "))
    n = int(input("Enter a number: "))

    if choice == 1:
        print(is_palindrome(n))
    elif choice == 2:
        print(reverse_integer(n))
    elif choice == 3:
        print(is_power_of_two(n))
    elif choice == 4:
        print(is_ugly(n))
    elif choice == 5:
        print(is_happy(n))
    elif choice == 6:
        print(count_primes(n))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
