from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR1 = decode(Image.open('qrcode_valid.jpg'))
print("VALID QR CODE")
print(decocdeQR1[0].data.decode('ascii'))

decocdeQR2 = decode(Image.open('qrcode_invalid.png'))
if (decocdeQR2):
    print(decocdeQR2[0].data.decode('ascii'))
else:
    print("INVALID QR CODE")
