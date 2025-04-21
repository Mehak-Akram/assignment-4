import qrcode

def generate_qr(data, filename="sample_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    text = input("Enter the text or URL to encode: ")
    generate_qr(text)

