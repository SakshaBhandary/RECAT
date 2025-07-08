from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.show()
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((0, 0), "User: Ramya", font=font, fill=255)
draw.text((0, 20), "Temp: 36.4C", font=font, fill=255)

display.image(image)
display.show()