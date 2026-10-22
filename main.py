# QR-CODE GENERATOR 
import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data('https://atman3023.github.io/message-QR-generator-V1/')
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="deeppink", back_color="white")

# Save the image
img.save("message.png")