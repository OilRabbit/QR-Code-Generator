import pyqrcode
import png
from pyqrcode import QRCode

s = input("Please paste the URL of the webside you would like to generate a QR Code for \n")
# print("\n")
name = input("Please input the name of the QR Code \n")
# print("\n")


url = pyqrcode.create(s)
url.svg(name, scale = 8)
url.png(name, scale = 6)
