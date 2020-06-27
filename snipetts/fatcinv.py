
class FactInv:
    def __init__(self, N, MOD=1000000007):
        fact = [1]*(N+1)
        for i in range(1, N+1):
            fact[i] = fact[i - 1] * i % MOD

        inv = [None]*(N+1)
        inv[N] = pow(fact[N], MOD - 2, MOD)

        for i in range(N)[::-1]:
            inv[i] = inv[i + 1] * (i + 1) % MOD

        self.N = N
        self.MOD = MOD
        self.fact = fact
        self.inv = inv

    def perm(self, a, b):
        if a > self.N or b > self.N:
            raise ValueError(
                "\nPermutaion arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[a-b] % self.MOD

    def comb(self, a, b):
        if a > self.N or b > self.N:
            raise ValueError(
                "\nCombination arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[b] * self.inv[a-b] % self.MOD

