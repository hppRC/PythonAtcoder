# nodeをリストに変換したらクソ遅かった

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def __str__(self):
        def debug_info(nd):
            return (nd.value - 1, nd.left.value - 1 if nd.left else None, nd.right.value - 1 if nd.right else None)

        def debug_node(nd):
            v = debug_info(nd) if nd.value else ()
            left = debug_node(nd.left) if nd.left else []
            right = debug_node(nd.right) if nd.right else []
            return [v, left, right]

        return pprint.PrettyPrinter(indent=4).pformat(debug_node(self.root))

    __repr__ = __str__

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            # v がすでに存在する場合に何か処理が必要ならここに書く
            if v == nd.value:
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        return self.leftmost(nd.left) if nd.left else nd

    def rightmost(self, nd):
        return self.rightmost(nd.right) if nd.right else nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = nd.value if nd.value < v else 0
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = nd.value if nd.value > v else 0
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def max(self):
        return self.find_l((1<<self.N)-1)

    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd:
            nd = self.root
        if not prev:
            prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        if (not nd.left) and (not nd.right):
            if nd.value < prev.value:
                prev.left = None
            else:
                prev.right = None
        elif not nd.left:
            if nd.value < prev.value:
                prev.left = nd.right
            else:
                prev.right = nd.right
        elif not nd.right:
            if nd.value < prev.value:
                prev.left = nd.left
            else:
                prev.right = nd.left
        else:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None