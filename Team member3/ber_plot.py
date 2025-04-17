import matplotlib.pyplot as plt

def plot_ber_vs_snr(snr_db_list, ber_list):
    plt.plot(snr_db_list, ber_list, marker='o')
    plt.xlabel("SNR (dB)")
    plt.ylabel("Bit Error Rate")
    plt.title("BER vs SNR")
    plt.grid(True)
    plt.show()
