def map_bits_to_iq(bits, M):
    import numpy as np
    k = int(np.log2(M))
    # Convert to decimal then map to I/Q
    symbols = [int("".join(map(str, bits[i:i+k])), 2) for i in range(0, len(bits), k)]
    return [(s % np.sqrt(M), s // np.sqrt(M)) for s in symbols]
