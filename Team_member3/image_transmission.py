from PIL import Image
import numpy as np

def image_to_bits(image_path):
    img = Image.open(image_path).convert("L")
    arr = np.array(img).flatten()
    bits = [int(b) for byte in arr for b in format(byte, '08b')]
    return bits, img.size

def bits_to_image(bits, size):
    pixels = [int("".join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8)]
    arr = np.array(pixels, dtype=np.uint8).reshape(size[::-1])
    return Image.fromarray(arr)
