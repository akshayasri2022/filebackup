import qrcode
from PIL import Image, ImageDraw
data = input("enter a text or url: ").strip()
filename = input("enter a file name: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
