class ModInt:
    def __init__(self, x, MOD=1000000007): self.x, self.MOD = x % MOD, MOD
    def __str__(self): return str(self.x)
    def __add__(self, other): return ModInt(self.x + other.x) if isinstance(other, ModInt) else ModInt(self.x + other)
    def __sub__(self, other): return ModInt(self.x - other.x) if isinstance(other, ModInt) else ModInt(self.x - other)
    def __mul__(self, other): return ModInt(self.x * other.x) if isinstance(other, ModInt) else ModInt(self.x * other)
    def __truediv__(self, other): return ModInt(self.x * other.inverse()) if isinstance(other, ModInt) else ModInt(self.x * pow(other, self.MOD - 2, self.MOD))
    def __pow__(self, other): return ModInt(pow(self.x, other.x, self.MOD)) if isinstance(other, ModInt) else ModInt(pow(self.x, other, self.MOD))
    def __rsub__(self, other): return ModInt(other.x - self.x) if isinstance(other, ModInt) else ModInt(other - self.x)
    def __rtruediv__(self, other): return ModInt(other.x * other.inverse()) if isinstance(other, ModInt) else ModInt(other * pow(self.x, self.MOD - 2, self.MOD))
    def __rpow__(self, other): return ModInt(pow(other.x, self.x, self.MOD)) if isinstance(other, ModInt) else ModInt(pow(other, self.x, self.MOD))
    __repr__, __radd__, __rmul__ = __str__, __add__, __mul__
    def inverse(self): return pow(self.x, self.MOD - 2, self.MOD)