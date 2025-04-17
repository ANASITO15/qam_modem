def calculate_ber(original, received):
    length = min(len(original), len(received))
    if length == 0:
        return 0  # or raise an error if that's more appropriate
    errors = sum(o != r for o, r in zip(original[:length], received[:length]))
    return errors / length

def calculate_snr(signal, noise):
    import numpy as np
    signal_power = np.mean(np.array(signal)**2)
    noise_power = np.mean(np.array(noise)**2)
    return 10 * np.log10(signal_power / noise_power)
