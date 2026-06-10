from PIL import Image

def bits_to_int(bits):
    n = 0
    for bit in bits:
        n = (n << 1) | bit
    return n

def bits_to_bytes(bits):
    out = bytearray()
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            break
        out.append(bits_to_int(byte_bits))
    return bytes(out)

def reveal_image_from_image(hidden_path, output_path):
    img = Image.open(hidden_path).convert("RGB")
    bits = []
    for r, g, b in img.get_flattened_data():
        bits.extend([r & 1, g & 1, b & 1])

    width = bits_to_int(bits[:32])
    height = bits_to_int(bits[32:64])

    num_data_bits = width * height * 3 * 8
    data_bits = bits[64:64 + num_data_bits]
    secret_bytes = bits_to_bytes(data_bits)

    secret_img = Image.frombytes("RGB", (width, height), secret_bytes)
    secret_img.save(output_path)
    print(f"Recovered hidden image and saved to {output_path}")

if __name__ == "__main__":
    reveal_image_from_image("hidden_image_stego.png", "revealed_secret_image.png")
