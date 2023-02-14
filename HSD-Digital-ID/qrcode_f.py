import os
import sys
import qrcode
import PIL

"""
Erst wird der Pfad des Scripts gespeichert, um durch diesen den Pfad zum Ordner,
wo die Qr Codes gespeichert sind zu kriegen
"""
current_path = os.path.dirname(__file__)
qr_codes_folder = f"{current_path[:-14]}Datasets\\qr_codes"


"""
Funktion, welche einen QR-Code erstellt und als png-Datei speichert.
Parameter inhalt; ist der Inhalt des QR-Codes
Parameter name; ist der Name der erstellten png-Datei 
"""

def make_qr(content,
            name):
    qr = qrcode.QRCode()
    qr.add_data(content)
    img = qr.make_image()
    img.save(f"{qr_codes_folder}\\{name}.png")
    #img.show()


