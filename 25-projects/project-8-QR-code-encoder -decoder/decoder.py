import cv2

def decode_qr(image_path):
    
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        print("QR Code detected.")
        print("Decoded data:", data)
    else:
        print("No QR Code found.")

if __name__ == "__main__":
    path = input("Enter the path to the QR code image: ")
    decode_qr(path)
