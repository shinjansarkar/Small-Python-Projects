import qrcode # type: ignore
text=input("Enter The Text- ")
img = qrcode.make(text)
img.save("Qr_code1.png") 