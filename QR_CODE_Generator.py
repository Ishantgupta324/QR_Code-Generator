import qrcode
url = input("Enter the URL : ").strip()
img = qrcode.make(url)
img.save("QR_Code.png")
print("QR code saved as QR_Code.png")