import qrcode
data="www.google.com"
qr=qrcode.make(data,version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=2)
qr.save("qr_code.png")
print("QR generated see your current directory")
