# QR code project
##import qrcode
##import cv2
##from PIL import Image
##img = qrcode.make("https://bareburger.com/menu")
##img.save("youtubeQR.jpg")

##d = cv2.QRCodeDetector()
##val, _, _ = d.detectAndDecode(cv2.imread("/Users/banegryphon/PycharmProjects/pythonProject1/youtubeQR.jpg"))
###print("Decoded text is: ", val)

#------------ END QR CODE GENERATOR -----------------#

#------------ BEGIN PICTURE FILTER -----------------#
import cv2

image = cv2.imread(/Users/banegryphon/PycharmProjects/pythonProject1/venv/test1/image.jpeg)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(image)








