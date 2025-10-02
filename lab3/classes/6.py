def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

nums = input("Введите числа через пробел: ")
numbers = [int(x) for x in nums.split()]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Простые числа из списка:", prime_numbers)
