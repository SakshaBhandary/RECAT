import board
import busio
import adafruit_mlx90614

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mlx90614.MLX90614(i2c)

while True:
    temp = sensor.object_temperature
    print(f"Object Temp: {temp:.2f} C")