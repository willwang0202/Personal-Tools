import qrcode

def generate_qr_code(link, filename):
    """Generates a QR code for the given link and saves it as filename."""

    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QR Code.png")

if __name__ == "__main__":
    userInput = input("Please input the URL: ")
    generate_qr_code(userInput, "Profile.png")
    print(f"QR code saved successfully!!")