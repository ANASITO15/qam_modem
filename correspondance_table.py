import pandas as pd
import numpy as np

def generate_table(M, use_gray=True):
    symbols = np.arange(M)
    bits_per_symbol = int(np.log2(M))
    gray_symbols = [symbol ^ (symbol >> 1) for symbol in symbols] if use_gray else symbols
    iq = [(i % np.sqrt(M), i // np.sqrt(M)) for i in gray_symbols]
    energy = [i**2 + q**2 for i, q in iq]
    phase = [np.arctan2(q, i) for i, q in iq]
    return pd.DataFrame({
        'Symbol': symbols,
        'Gray': gray_symbols,
        'I': [i for i, _ in iq],
        'Q': [q for _, q in iq],
        'Energy': energy,
        'Phase': phase
    })
