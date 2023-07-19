import segno as sg

qrCode = ''
processDone = False

print("Type something for your QRCode, since a simple phrase up to a URL")
userPhrase = input("Type > ")

print("Now, give a name for your QR Code file")
userFile = input("Type > ")
qrName = sg.make(userPhrase)

print("Finally, choose a format file the QR Code will be saved.")
print("[1] - SVG")
print("[2] - PNG")
print("[3] - PDF")

qrFile = int(input("Select > "))

while processDone == False:
    if qrFile == 1: 
        file = '.svg'

        qrExport = (f'{userFile}{file}')
        print("Will be saved as SVG")
        qrName.save(qrExport, scale = 10)
        processDone = True

    elif qrFile == 2:
        file = '.png'

        qrExport = (f'{userFile}{file}')
        print("Will be saved as PNG")
        qrName.save(qrExport, scale = 10)
        processDone = True

    elif qrFile == 3:
        file = '.pdf'

        qrExport = (f'{userFile}{file}')
        print("Will be saved as PDF")
        qrName.save(qrExport, scale = 10)
        processDone = True
    else:
        print("Format invalid. Choose one of the following options")
        print("[1] - SVG")
        print("[2] - PNG")
        print("[3] - PDF")
        qrFile = int(input("Select > "))