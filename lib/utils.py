def bitgen(x):
    """
    :params x: Iterable chars stream.
    :returns: Generator which converts chars into string of bits.
    """
    for c in x:
        for i in range(8):
            yield int((c & (0x80 >> i)) != 0)
