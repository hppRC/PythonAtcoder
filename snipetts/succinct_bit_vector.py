print(0xFFFFFFFFFFFFFFFF)

class SuccinctBitVector:
    def __init__(self, n):
        self.size = 0
        self.block_bit_num = 16
        self.LEVEL_L = 512
        self.LEVEL_S = 16
        self.num_one = 0  # 1bitの数

        s = (n + self.block_bit_num - 1) // self.block_bit_num + 1   # ceil(n, blockSize)
        self.B = [0] * s
        self.L = [0] * (n // self.LEVEL_L + 1)
        self.S = [0] * (n // self.LEVEL_S + 1)
        self.build()

    def build(self):
        num = 0
        for i in range(self.size+1):
            if (i % self.LEVEL_L == 0):
                self.L[i // self.LEVEL_L] = num
            if (i % self.LEVEL_S == 0):
                self.S[i // self.LEVEL_S] = num - self.L[i // self.LEVEL_L]
            if (i != self.size and i % self.block_bit_num == 0):
                num += self.pop_count(self.B[i // block_bit_num])

        self.num_one = num

    def pop_count(self, x):
        x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
        x = x + (x >>  8)
        x = x + (x >> 16)
        x = x + (x >> 32)
        return x & 0x7F



sbv = SuccinctBitVector(50)
print(sbv.B)
print(sbv.L)
print(sbv.S)