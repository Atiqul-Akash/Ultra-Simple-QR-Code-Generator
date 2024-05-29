import qrcode
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 20, border = 6)
userInput = input("Enter Your Text-> ")
qr.add_data(userInput)
img = qr.make_image(fill_color = "red", back_color = "black")
img.save("QR Code.jpg")