import qrcode

# Function to generate QR code for a website
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
url = "https://www.ivrs.se"  # Replace with your website URL
filename = "/Users/sbk/Documents/IVRS/Website/" + "websiteQR.png"  # Replace with desired filename
generate_qr_code(url, filename)
print(f"QR code saved as '{filename}'")
