import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://www.youtube.com/")
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")
img.save("YouTube_QR.png")







# This is the Basic of generate a QR code...

# import generate_qr as qr

# img = qr.make("Hello ! I'm Souren Roy ") 
# # you can provide link/text

# img.save("Image.png")
