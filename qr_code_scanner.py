import cv2
import json
from pyzbar.pyzbar import decode


with open("product_data_full.json", "r") as f:
    product_data = json.load(f)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    for barcode in decode(frame):
        product_id = barcode.data.decode("utf-8")
        if product_id in product_data:
            product = product_data[product_id]

            image = cv2.imread(product["image"])
            if image is None:
                print(f"Image not found: {product['image']}")
                break

            # Resize for display
            image = cv2.resize(image, (600, 400))

            # Add text info to the image
            y = 30
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.6
            color = (0, 255, 0)
            thickness = 1

            cv2.putText(image, f"Name: {product['name']}", (10, y), font, font_scale, color, thickness)
            y += 25
            cv2.putText(image, f"Price: ₹{product['price']}", (10, y), font, font_scale, color, thickness)
            y += 25
            cv2.putText(image, f"Brand: {product['brand']}", (10, y), font, font_scale, color, thickness)
            y += 25
            cv2.putText(image, f"Stock: {product['stock']}", (10, y), font, font_scale, color, thickness)
            y += 25
            cv2.putText(image, f"Rating: {product['rating']} ⭐", (10, y), font, font_scale, color, thickness)
            y += 25
            cv2.putText(image, f"Desc: {product['description'][:50]}...", (10, y), font, font_scale, color, thickness)

            cv2.imshow("Product Info", image)

            print(f"\n Product '{product['name']}' scanned successfully!")
            cap.release()
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("QR Code Scanner - Press 'q' to Quit", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
