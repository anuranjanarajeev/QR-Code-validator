import pyqrcode
qr = pyqrcode.create("HORN O.K. PLEASE.")
qr.png("horn.png", scale=6)
