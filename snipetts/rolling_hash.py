# thanks to: https://drken1215.hatenablog.com/entry/2019/09/16/014600

class DoubleRollingHash:
    def __init__(self, seq, f=ord):
        self.n = len(seq)
        self.base1, self.base2 = 1007, 2009
        self.mod1, self.mod2 = 1000000007, 1000000009
        self.f = f # set numerizing function

        self.hash1, self.hash2 = [0]*(self.n+1), [0]*(self.n+1)
        self.power1, self.power2 = [1]*(self.n+1), [1]*(self.n+1)

        for i, e in enumerate(seq):
            self.hash1[i+1] = (self.hash1[i] * self.base1 + self.f(e)) % self.mod1
            self.hash2[i+1] = (self.hash2[i] * self.base2 + self.f(e)) % self.mod2
            self.power1[i+1] = (self.power1[i] * self.base1) % self.mod1
            self.power2[i+1] = (self.power2[i] * self.base2) % self.mod2

    # get hash value of seq[left:right]
    def get(self, l, r):
        v1 = (self.hash1[r] - self.hash1[l] * self.power1[r-l]) % self.mod1
        v2 = (self.hash2[r] - self.hash2[l] * self.power2[r-l]) % self.mod2
        return v1, v2

    # get lcp of seq[a:] and seq[b:]
    def getLCP(self, a, b):
        l = self.n - max(a, b) + 1
        left, right = 0, l
        while right - left > 1:
            mid = (left + right) // 2
            if self.get(a, a+mid) == self.get(b, b+mid): left = mid
            else: right = mid
        return left


# https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
class RollingHash:
    def __init__(self, seq, f=ord):
        self.n = len(seq)
        self.base, self.mod = 1007, pow(2, 61) - 1
        self.f = f # set numerizing function
        self.hash, self.power = [0]*(self.n+1), [1]*(self.n+1)
        for i, e in enumerate(seq):
            self.hash[i+1] = (self.hash[i] * self.base + self.f(e)) % self.mod
            self.power[i+1] = (self.power[i] * self.base) % self.mod

    # get hash value of seq[left:right]
    def get(self, l, r): return (self.hash[r] - self.hash[l] * self.power[r-l]) % self.mod

    # get lcp of seq[a:] and seq[b:]
    def getLCP(self, a, b):
        l = self.n - max(a, b) + 1
        left, right = 0, l
        while right - left > 1:
            mid = (left + right) // 2
            if self.get(a, a+mid) == self.get(b, b+mid): left = mid
            else: right = mid
        return left