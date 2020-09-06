class ZAlgo:
    def __init__(self, seq):
        self.n = len(seq)
        # seq 自身と seq[i:] とが、先頭から最大で何文字一致しているか
        self.lcp = [0] * self.n
        self.lcp[0] = self.n
        i, j = 1, 0
        while i < self.n:
            while i + j < self.n and seq[j] == seq[i+j]:
                j += 1
            self.lcp[i] = j
            if j == 0:
                i += 1
                continue

            k = 1
            while i + k < self.n and k + self.lcp[k] < j:
                self.lcp[i + k] = self.lcp[k]
                k += 1
            i += k
            j -= k

    # seq[0:]とseq[i:]のLCP
    def getLCP(self, i): return self.lcp[i]