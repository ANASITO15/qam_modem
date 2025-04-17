def add_awgn(iq, snr_db):
    import numpy as np
    snr = 10**(snr_db/10)
    signal_power = np.mean([i**2 + q**2 for i, q in iq])
    noise_power = signal_power / snr
    noise_std = np.sqrt(noise_power / 2)
    noisy_iq = [(i + np.random.normal(0, noise_std),
                 q + np.random.normal(0, noise_std)) for i, q in iq]
    return noisy_iq
