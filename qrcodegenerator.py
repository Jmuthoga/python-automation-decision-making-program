import qrcode
import image

qr = qrcode.QRCode(
    version=15, #15 means the versionof the qr code high the number bigger the code image and complicated picture. 
    box_size=10, #size of the box where the qr code will be displayed.
    border=5 #is the white part of the image ---border in all 4 sides with white color
)

data = "https://github.com/Jmuthoga"
#as I have given the path of my github channel

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("text.png")
