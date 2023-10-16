"""Compression"""
import math
import sys
from collections import defaultdict

from typing_extensions import Self

from lib.utils import bitgen, byterange, bytesize, create_arg_parser


class Node:
    """Node of a binary tree

    :param w: Weight of the node; frequency of appearance.
    :param v: Symbol value.
    :param childs: Children of the node.
    """

    def __init__(self, w: int, v: str = None, childs: list[Self] = [None, None]):
        self.w = w
        self.v = v
        self.childs = childs
        self.enc = ""

    def __repr__(self):
        return f"({self.v}) {self.w} : {self.enc}"

    def tree(self, level=0):
        ret = "\t" * level + self.v + "\n"
        for c in self.childs:
            if c is not None:
                ret += c.tree(level + 1)
        return ret


def huffman(enw: bytes) -> int:
    """Huffman coding.

    :param enw: Input bytes stream.
    :returns: Binary encoded input stream.
    """
    lt = defaultdict(lambda: 0)
    for c in enw:
        lt[c] += 1

    lt = dict(sorted(lt.items(), key=lambda kv: kv[1]))

    ns = [Node(v, chr(k)) for k, v in lt.items()]

    while len(ns) > 1:
        left = ns.pop(0) if ns else None
        right = ns.pop(0) if ns else None

        nn = Node(w=((left.w + right.w)), childs=[left, right])

        idx = next((i for i, x in enumerate(ns) if nn.w <= x.w), len(ns))
        ns.insert(idx, nn)

    def enc(n: Node, res: list[Node] = []):
        """Finding encodings using the depth-first search algorithm."""
        if n is None:
            return
        for idx, c in enumerate(n.childs):
            if c is not None:
                c.enc = n.enc + str(idx)
        if n.v is not None:
            res.append(n)
        for c in n.childs:
            enc(c, res)

        return res

    # compute the encodings.
    encs = enc(ns[0])

    # return the encoded input.
    return int("".join(next(x.enc for x in encs if x.v == chr(c)) for c in enw), base=2)


def main():
    enw = open("data/enwik4", "rb").read()
    bg = bitgen(enw)

    number_of_bits = 16
    lookup = defaultdict(lambda: [1, 2])
    HH = 0.0

    try:
        prevx = [-1] * number_of_bits
        while True:
            x = next(bg)

            px = tuple(prevx)

            p_1 = lookup[px][0] / lookup[px][1]
            p_x = p_1 if x == 1 else 1.0 - p_1

            H = -math.log2(p_x)
            HH += H

            lookup[px][0] += x == 1
            lookup[px][1] += 1
            prevx.append(x)
            prevx = prevx[-number_of_bits:]

    except StopIteration:
        pass

    print(f"information entropy: {HH/8.0:.1f}")


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args(sys.argv[1:])

    if data := args.d:
        enw = open(data, "rb").read()
    else:
        print("No data file specified. Use -d <file>")
        exit(1)

    if args.a == "huffman":
        encs = huffman(enw)
    else:
        print("No algorithm specified. Use -a <algorithm>")
        exit(1)

    # Output the results.
    benw = bytesize(enw)
    bencs = bytesize(encs)
    print(
        f"res: {byterange(bencs)} ({byterange(benw)}), compression ratio: {bencs/benw:.2f}"
    )
