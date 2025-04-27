import json
import qrcode
import os


with open("product_data_full.json", "r") as f:
    product_data = json.load(f)


qr_folder = "qr_codes"
os.makedirs(qr_folder, exist_ok=True)


for product_id in product_data:
    qr = qrcode.make(product_id)  
    qr_path = os.path.join(qr_folder, f"{product_id}.png")
    qr.save(qr_path)

print(" All QR codes generated and saved in the 'qr_codes' folder.")
