from PIL import Image

def reveal_message_lsb(image_path):
    image = Image.open(image_path).convert("RGB")
    bits = []

    for r, g, b in image.get_flattened_data():
        bits.append(str(r & 1))
        bits.append(str(g & 1))
        bits.append(str(b & 1))

    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break

        chars.append(chr(int("".join(byte), 2)))
        message = "".join(chars)

        if "###END###" in message:
            return message.replace("###END###", "")

    return "".join(chars)

if __name__ == "__main__":
    message = reveal_message_lsb("hidden_message_image.png")
    print(message)
