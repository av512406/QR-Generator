import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "Anand Vishwakarma B20028"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png("B20028.png", scale = 8) 
# print(url.terminal(quiet_zone=1))