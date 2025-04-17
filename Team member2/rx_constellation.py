import numpy as np
def demodulate_iq(iq_points, M):
    # Map back to nearest symbol
    # Simplified distance-based decoding
    return [round(i) + round(q) * int(np.sqrt(M)) for i, q in iq_points]
