import board
import busio
import adafruit_bme680

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)


def to_fahrenheit(celsius: int) -> int:
    """Converts a celsius measurement to Farenheit.

    Arguments:
        celsius {int} -- the measurment in celsius

    Returns:
        int -- the equivalent measurement in Farenheit
    """
    return celsius * (9/5) + 32


def data_dict(fahrenheit=True):
    """Fetches the data from the Raspberry Pi's sensors, packages, and returns it

    Keyword Arguments:
        fahrenheit {bool} -- whether or not to convert the sensor measurments
                            to Farenheit (default: {True})

    Returns:
        dict -- a dict containing measurements for temperature, humidity, and
                airPressure
    """

    temp = round(sensor.temperature, 2)
    if fahrenheit:
        temp = to_fahrenheit(temp)

    return {
        'temperature': temp,
        'humidity': sensor.humidity,
        'airPressure': sensor.pressure,
    }

    # Used for testing w/o Raspberry Pi
    # return {
    #     'temperature': 10,
    #     'humidity': 11,
    #     'airPressure': 12,
    # }
