import qrcode

image = qrcode.make("https://127.0.0.1:5000")
image.save("qr.png")