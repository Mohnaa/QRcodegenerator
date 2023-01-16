import qrcode
import image
qr = qrcode.QRCode(
    version= 15,   #15 meansthe verrsion of the qr code, high the number bigger the code image and complicated picture
    box_size = 10, #size of the box where qrcode will be displayed
    border = 5 #it is the white part of image--> border in all 4 sides with white color

)
data ="https://mohnaa.netlify.app/"
#i have given the path of my portfolio

#if u don't want to redirect and create for normal text that write text in the quotes
qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill_color="black", back_color = "white")
img.save("test.png")