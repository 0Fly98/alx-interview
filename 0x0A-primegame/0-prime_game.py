def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if (is_prime[p] == True):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
    return prime_numbers

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_n)
    wins = {'Maria': 0, 'Ben': 0}

    def play_game(n):
        nums = [i for i in range(1, n+1)]
        primes_removed = set()
        turn = 0  # Maria starts first, turn % 2 == 0 means Maria's turn
        
        for prime in prime_numbers:
            if prime > n:
                break
            if prime not in primes_removed:
                # Remove prime and its multiples
                multiple = prime
                while multiple <= n:
                    if multiple in nums:
                        nums.remove(multiple)
                        primes_removed.add(multiple)
                    multiple += prime
                turn += 1
        
        return 'Maria' if turn % 2 == 1 else 'Ben'

    for n in nums:
        winner = play_game(n)
        wins[winner] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None

