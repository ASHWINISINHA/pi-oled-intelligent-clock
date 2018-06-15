import time
import os,time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from time import gmtime, strftime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
showtime = strftime("%a  %d %b  %Y time %X second",gmtime())
# 128x32 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()

# Clear display.
disp.clear()
disp.display()


width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Draw an ellipse.

# Load default font.
font = ImageFont.load_default()
font = ImageFont.truetype('Montserrat-Light.ttf', 14)
font2 = ImageFont.truetype('Montserrat-Light.ttf', 20)
font_text_big = ImageFont.truetype('Montserrat-Medium.ttf', 30)

while True:
     draw.rectangle((0,0,width,height), outline=0, fill=0)     
     draw.text((x, top),    str(strftime("%a  %d %b  %Y ",gmtime())), font=font, fill=455)
     draw.text((x, top+39),    str(strftime("%a  %d ",gmtime())), font=font2, fill=455)
     draw.text((x, top+12), str(strftime("%X",gmtime())), font=font_text_big, fill=455)

     disp.image(image)
     disp.display()
