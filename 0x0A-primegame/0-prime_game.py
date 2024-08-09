#!/usr/bin/python3
"""Island perimeter computing module.
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0], primes[1] = False, False

        for num in range(2, int(limit**0.5) + 1):
            if primes[num]:
                for multiple in range(num*num, limit + 1, num):
                    primes[multiple] = False

        return [num for num, is_prime in enumerate(primes) if is_prime]

    def can_make_move(num, primes):
        for prime in primes:
            if prime > num:
                break
            if num % prime == 0:
                return True
        return False

    wins = {'Maria': 0, 'Ben': 0}
    max_num = max(nums)
    all_primes = sieve_of_eratosthenes(max_num)

    for n in nums:
        if can_make_move(n, all_primes):
            wins['Maria' if x % 2 == 1 else 'Ben'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
