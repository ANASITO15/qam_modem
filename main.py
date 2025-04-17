import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


M = 16
snr_values = list(range(0, 21, 2))  # From 0dB to 20dB in 2dB steps
from Team_member3.image_transmission import image_to_bits

bits, size = image_to_bits("hhaw7sc3vad51.png")  # or generate random bits
# bits = [random.randint(0, 1) for _ in range(1000)]  # Example random bits


from Team_member2.tx_constellation import map_bits_to_iq

iq_symbols = map_bits_to_iq(bits, M)
print("IQ Symbols:", iq_symbols)



from Team_member2.noise_simulation import add_awgn
from Team_member2.rx_constellation import demodulate_iq
from Team_member3.ber_snr import calculate_ber

ber_list = []

for snr in snr_values:
    noisy_iq = add_awgn(iq_symbols, snr)
    symbols_rx = demodulate_iq(noisy_iq, M)
    
    # Convert symbols back to bits (implement this function or use a placeholder)
    received_bits = []  # placeholder

    ber = calculate_ber(bits[:len(received_bits)], received_bits)
    ber_list.append(ber)


from Team_member3.ber_plot import plot_ber_vs_snr

plot_ber_vs_snr(snr_values, ber_list)


from Team_member3.image_transmission import bits_to_image

output_image = bits_to_image(received_bits, size)
output_image.save("output_image.png")
output_image.show()