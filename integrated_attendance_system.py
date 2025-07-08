import face_recognition
import cv2
import board
import busio
import adafruit_mlx90614
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Load known faces
known_faces = []
known_names = []
for name in os.listdir("known_faces"):
    img = face_recognition.load_image_file(f"known_faces/{name}")
    enc = face_recognition.face_encodings(img)[0]
    known_faces.append(enc)
    known_names.append(os.path.splitext(name)[0])

# Initialize I2C sensors
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mlx90614.MLX90614(i2c)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Setup camera
camera = cv2.VideoCapture(0)

def send_email(name, temp):
    body = f"Alert! {name} has a high temperature: {temp:.2f}C"
    msg = MIMEText(body)
    msg["Subject"] = "Covid Alert - Temperature"
    msg["From"] = "sender@example.com"
    msg["To"] = "admin@example.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("sender@example.com", "your-password")
        server.send_message(msg)

def log_data(name, temp):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("attendance_log.csv", "a") as file:
        file.write(f"{timestamp},{name},{temp:.2f}\n")

while True:
    ret, frame = camera.read()
    rgb = frame[:, :, ::-1]
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for (top, right, bottom, left), enc in zip(locations, encodings):
        matches = face_recognition.compare_faces(known_faces, enc)
        name = "Unknown"
        if True in matches:
            name = known_names[matches.index(True)]
            temp = sensor.object_temperature
            log_data(name, temp)
            if temp > 37.5:
                send_email(name, temp)

            # OLED display
            image = Image.new("1", (display.width, display.height))
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            draw.text((0, 0), f"Name: {name}", font=font, fill=255)
            draw.text((0, 20), f"Temp: {temp:.1f}C", font=font, fill=255)
            display.image(image)
            display.show()

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Covid Secure Recat", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()