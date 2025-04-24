from flask import Flask, request, jsonify, send_file,  render_template
import os
import numpy as np
from werkzeug.utils import secure_filename

# Import your functions (adapt imports as needed)
from Team_member3.image_transmission import image_to_bits, bits_to_image
from Team_member2.tx_constellation import map_bits_to_iq
from Team_member2.noise_simulation import add_awgn
from Team_member2.rx_constellation import demodulate_iq
from Team_member3.ber_snr import calculate_ber

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')  # Flask will look in 'templates/' folder

@app.route('/simulate', methods=['POST'])
def simulate():
    file = request.files.get('image')
    modulation_order = int(request.form.get('modulation', 16))

    if not file:
        return jsonify({"error": "No image uploaded"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    bits, size = image_to_bits(filepath)
    iq_symbols = map_bits_to_iq(bits, modulation_order)
    snr_values = list(range(0, 21, 2))
    ber_list = []

    for snr in snr_values:
        noisy_iq = add_awgn(iq_symbols, snr)
        symbols_rx = demodulate_iq(noisy_iq, modulation_order)

        # Convert symbols back to bits
        bits_per_symbol = int(np.log2(modulation_order))
        received_bits = []
        for s in symbols_rx:
            b = format(int(s), f'0{bits_per_symbol}b')
            received_bits.extend([int(bit) for bit in b])

        ber = calculate_ber(bits[:len(received_bits)], received_bits)
        ber_list.append(ber)

    # Reconstruct image
    output_img = bits_to_image(received_bits[:len(bits)], size)
    
    print("Saving image as output_image.png in", os.getcwd())
    output_img.save("output_image.png")
    print("Image saved.")
    output_img.show()

    return jsonify({
        "snr": snr_values,
        "ber": ber_list
    })


@app.route('/output_image.png')
def get_output_image():
    return send_file('output_image.png', mimetype='image/png')



if __name__ == '__main__':
    app.run(debug=True)
