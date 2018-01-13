import time 

#Displaay
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

#Buttons
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Stocks
from rtstock.stock import Stock
 
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded = 4, block_orientation = -90)
 
padPin1 = 23
padPin2 = 24
padPin3 = 25 
padPin4 = 26

GPIO.setup(padPin1, GPIO.IN)
GPIO.setup(padPin2, GPIO.IN)
GPIO.setup(padPin3, GPIO.IN)
GPIO.setup(padPin4, GPIO.IN)

while True:
        
    if GPIO.input(padPin1):
        print ("pressed pad 1")
        choice = 1
    
    elif GPIO.input(padPin2):
        print ("pressed pad 2")
        choice = 2
        
    elif GPIO.input(padPin3):
        print ("pressed pad 3")
        choice = 3
        
    elif GPIO.input(padPin4):
        print ("pressed pad 4")
        choice = 4

    else:
        print("nothing pressed")
        choice = 0
    
    if choice = 2:
        aapl = Stock('AAPL')
        aapl_number = aapl.get_latest_price()
        print_number = aapl_number['LastTradePriceOnly']
            
        with canvas(device) as draw:
                    legacy.text(draw,(1,0),('{}'.format(print_number)) , fill = "white",font=proportional(LCD_FONT))
        
    else:
        current_time = time.strftime("%M:%S")
        array_of_time = list(current_time)

        with canvas(device) as draw:
            for i in range(5):
                if i == 3 or i == 4 :
                    legacy.text(draw,(i*6,0),array_of_time[i], fill = "white",font=proportional(LCD_FONT))
                else:
                    legacy.text(draw,(3+(i*6), 0), array_of_time[i], fill = "white",font=proportional(LCD_FONT))
