class NTT:
    '''
        conv: ci = ∑_{j=0}^i a_j * b_{i−j} % mod
        添字の和がiになるajとbkの積の和
    '''

    def __init__(self, a, b, mod=998244353, root=3):
        self.mod, self.root = mod, root
        deg = len(a) + len(b) - 2
        self.n = deg.bit_length()
        N = 1 << self.n
        self.roots  = [pow(self.root, (self.mod-1)>>i, self.mod) for i in range(24)] # 1 の 2^i 乗根
        self.iroots = [pow(x,self.mod-2,self.mod) for x in self.roots] # 1 の 2^i 乗根の逆元

        self.conv = a + [0]*(N-len(a))
        self.b = b + [0]*(N-len(b))

        self.untt()
        self.untt(False)
        for i in range(N):
            self.conv[i] = self.conv[i] * self.b[i] % self.mod
        self.iuntt()
        del self.conv[deg+1:] # inplace ver. of self.conv[:deg+1]

    def untt(self, flag=True):
        a = self.conv if flag else self.b
        for i in range(self.n):
            m = 1 << (self.n - i - 1)
            for s in range(1 << i):
                W = 1
                s *= m * 2
                for p in range(m):
                    a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]) % self.mod, (a[s+p]-a[s+p+m]) * W % self.mod
                    W = W * self.roots[self.n-i] % self.mod

    def iuntt(self):
        for i in range(self.n):
            m = 1 << i
            for s in range(1 << (self.n-i-1)):
                W = 1
                s *= m * 2
                for p in range(m):
                    self.conv[s+p], self.conv[s+p+m] = (self.conv[s+p]+self.conv[s+p+m]*W)%self.mod, (self.conv[s+p]-self.conv[s+p+m]*W)%self.mod
                    W = W * self.iroots[i+1] % self.mod
        inv = pow((self.mod + 1) // 2, self.n, self.mod)
        for i in range(1<<self.n):
            self.conv[i] = self.conv[i] * inv % self.mod

class OutplaceNTT:
    '''
        conv: ci = ∑_{j=0}^i a_j * b_{i−j} % mod
        添字の和がiになるajとbkの積の和
    '''

    def __init__(self, a, b, mod=998244353, root=3):
        self.mod, self.root = mod, root
        self.deg = len(a) + len(b) - 2
        self.n = self.deg.bit_length()
        self.N = 1 << self.n
        self.roots  = [pow(self.root, (self.mod-1)>>i, self.mod) for i in range(24)] # 1 の 2^i 乗根
        self.iroots = [pow(x,self.mod-2,self.mod) for x in self.roots] # 1 の 2^i 乗根の逆元

        self.a = a + [0]*(self.N-len(a))
        self.b = b + [0]*(self.N-len(b))

        self.A = self.untt(self.a)
        self.B = self.untt(self.b)
        self.C = [self.A[i] * self.B[i] % self.mod for i in range(self.N)]
        self.conv = self.iuntt(self.C)[:self.deg+1]

    def untt(self, a):
        A = a[:]
        for i in range(self.n):
            m = 1 << (self.n - i - 1)
            for s in range(1 << i):
                W = 1
                s *= m * 2
                for p in range(m):
                    A[s+p], A[s+p+m] = (A[s+p]+A[s+p+m]) % self.mod, (A[s+p]-A[s+p+m]) * W % self.mod
                    W = W * self.roots[self.n-i] % self.mod
        return A

    def iuntt(self, A):
        a = A[:]
        for i in range(self.n):
            m = 1 << i
            for s in range(1 << (self.n-i-1)):
                W = 1
                s *= m * 2
                for p in range(m):
                    a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]*W)%self.mod, (a[s+p]-a[s+p+m]*W)%self.mod
                    W = W * self.iroots[i+1] % self.mod

        inv = pow((self.mod + 1) // 2, self.n, self.mod)
        for i in range(1<<self.n):
            a[i] = a[i] * inv % self.mod
        return a