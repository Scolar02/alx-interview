#!/usr/bin/python3
def isWinner(x, nums):
    def sieve_of_eratosthenes(max_num):
        sieve = [True] * (max_num + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_num**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_num + 1, i):
                    sieve[j] = False
        return [i for i in range(2, max_num + 1) if sieve[i]]

    # Precompute prime numbers up to the maximum number in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        available_nums = set(range(1, n + 1))
        current_turn = "Maria"

        while True:
            # Find the smallest prime in the available numbers
            prime_found = False
            for prime in primes:
                if prime in available_nums:
                    prime_found = True
                    # Remove the prime and its multiples from the available set
                    multiples = {prime * k for k in range(1, n // prime + 1)}
                    available_nums -= multiples
                    break

            if not prime_found:
                return "Ben" if current_turn == "Maria" else "Maria"

            # Switch turns
            current_turn = "Ben" if current_turn == "Maria" else "Maria"

    # Play x rounds and count wins
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
