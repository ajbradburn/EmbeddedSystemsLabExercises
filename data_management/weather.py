import math
import requests
import json
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from time import sleep
from datetime import datetime
import adafruit_ahtx0
import threading

class nws_forecast():
  # Get the National Weather Service Forecast based upon the Geolocation.
  # Geolocation is found by using the public IP address for the network that this device is attached to.
  def get(self):
    # Get the geolocation for your IP Address.
    # API Documentation: https://ip-api.com/docs/api:json
    URL = 'http://ip-api.com/json'
    
    r = requests.get(url = URL)
    data = r.json()
    # For debuggin purposes.
    #print(json.dumps(data, indent=2))
    latitude = data['lat']
    longitude = data['lon']
    
    # Get the National Weather Service Office, and grid for your location.
    # API Documentation: https://www.weather.gov/documentation/services-web-api#
    HEADERS = {'user-agent': '(IntroductionToEmbeddedSystems, ajbradburn@gmail.com)'}
    
    URL = 'https://api.weather.gov/points/{},{}'
    URL = URL.format(latitude, longitude)
    
    r = requests.get(url = URL, headers=HEADERS)
    
    data = r.json()
    # For debugging purposes.
    #print(json.dumps(data, indent=2))
    
    # Using the data from the last request, get the forcast for your area.
    office = data['properties']['gridId']
    loc_x = data['properties']['gridX']
    loc_y = data['properties']['gridY']
    
    URL = 'https://api.weather.gov/gridpoints/{}/{},{}/forecast'
    URL = URL.format(office, loc_x, loc_y)
    
    r = requests.get(url = URL, headers=HEADERS)
    
    data = r.json()
    # For debugging purposes.
    #print(json.dumps(data, indent=2))

    # Return only the current, or most immediate forecast.
    return data['properties']['periods'][0]

class oled_display():
  width = 128
  height = 32

  oled = None

  def __init__(self):
    self.oled = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, board.I2C(), addr=0x3C)

  def display_none(self):
    self.oled.fill(0)
    self.oled.show()

  def display_string(self, text, font = None, size = 10, height = None, width = None):
    image = Image.new("1", (self.oled.width, self.oled.height))

    draw = ImageDraw.Draw(image)

    if height == None or width == None:
      dimensions = self.text_size(text, font, size)
      
      if width == None:
        width = dimensions[0]

      if height == None:
        height = dimensions[1]

    if font == None:
      font = ImageFont.load_default()
    else:
      font = ImageFont.truetype(font, size)

    draw.text(
      (self.oled.width // 2 - width // 2, self.oled.height // 2 - height // 2),
      text,
      font=font,
      fill=10,
      )

    self.oled.image(image)
    self.oled.show()

  def text_size(self, text, font = None, size = 10):
    if font == None:
      font = ImageFont.load_default()
    else:
      font = ImageFont.truetype(font, size)
    return font.getsize(text)

  def scroll_string(self, text, font = None, size = 10, delay = 0.01):
    text_len = len(text)
    dimensions = self.text_size(text, font, size)
    window_length = math.floor(self.oled.width / (dimensions[0] / text_len))
    start = 0
    height = dimensions[1]
    width = window_length * (dimensions[0] / text_len)
    padding = ' ' * window_length
    text = padding + text + padding
    text_len = len(text)
    while start + window_length <= text_len:
      sub_string = text[start:start + window_length]
      start = start + 1
      self.display_string(sub_string, font, size, width=width, height=height)
      sleep(delay)
    return

  def display_with_intro(self, intro, text, font = None, size = 10):
    self.display_string(intro, font, size)
    sleep(1)
    self.scroll_string(text, font, size)

default_font = 'DejaVuSansMono.ttf'

# Initialize objects.
oled_display = oled_display()
sensor = adafruit_ahtx0.AHTx0(board.I2C())

def start_log_timer():
  log_timer = threading.Timer(30, log_measurements).start()

def start_forecast_timer():
  forecast_timer = threading.Timer(60, get_weather).start()

def start_temp_timer():
  global temp_timer
  temp_timer = threading.Timer(10, display_temp)
  temp_timer.start()

def get_weather():
  # Start a new timer.
  start_forecast_timer()

  # Cancel the temp_timer so that it doesn't interfere with our forecast display.
  global temp_timer
  temp_timer.cancel()

  # Get the forecast and display it.
  global oled_display
  global sensor
  weather = nws_forecast()
  forecast = weather.get()
  oled_display.display_string('High: {}°F'.format(forecast['temperature']), default_font, 16)
  sleep(2)
  oled_display.display_string('Inside: {}°F'.format(int(sensor.temperature * 9 / 5 + 32)), default_font, 16)
  sleep(2)
  oled_display.display_with_intro('Forecast:', forecast['detailedForecast'], default_font, 16)

  # Resume the display of temperature, and start a new temp_timer.
  display_temp()

def display_temp():
  # Start a new timer.
  start_temp_timer()

  # Read the temperature and display it.
  global default_font
  temperature = sensor.temperature
  humidity = sensor.relative_humidity
  oled_display.display_string('Inside: {:.2f}°F'.format(temperature * 9 / 5 + 32), default_font, 12)

def log_measurements():
  # Start a new timer.
  start_log_timer()

  # Read temperature and humidity. Log it with the date/time to a file in csv format.
  global sensor
  temperature = sensor.temperature
  humidity = sensor.relative_humidity
  string = '\"{}\",{:.2f},{:.2f}\n'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), temperature, humidity)
  file = open('log.csv', 'a')
  file.write(string)
  file.close()

# A variable to hold the temp_timer so that we can reference it later, and cancel the timer when needed.
temp_timer = None

start_log_timer()
display_temp()
start_forecast_timer()
