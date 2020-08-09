class Eratosthenes:
    # https://cp-algorithms.com/algebra/prime-sieve-linear.html
    def __init__(self, n):
        primes, lp = [], [0] * (n + 1)
        for i in range(2, n + 1):
            if lp[i] == 0:
                primes.append(i)
                lp[i] = i

            for pj in primes:
                if pj > lp[i] or i * pj > n: break
                lp[i * pj] = pj
        self.primes, self.lp = primes, lp

    def is_prime(self, x): return self.lp[x] == x

    def factors(self, x):
        ret = []
        while x > 1:
            ret.append(self.lp[x])
            x //= self.lp[x]
        return ret
