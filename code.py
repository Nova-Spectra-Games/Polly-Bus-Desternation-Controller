import board
import digitalio
import busio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from routes import arrays, Companys  # Import routes and companies from routes.py

# Initialize I2C and LCD
sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# Initialize buttons
button1 = digitalio.DigitalInOut(board.GP2)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP3)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.GP4)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

def main_screen():
    lcd.clear()
    lcd.print("Dest            Company")

# Function to check button state
def is_pressed(button):
    return not button.value

# Function to update LCD with the current item
def update_lcd(index):
    lcd.clear()
    lcd.print(items[index])

def update_lcd_comp(current_index2):
    lcd.clear()
    lcd.print(Companys[current_index2])
    return Companys[current_index2]

# Initial LCD messages
lcd.clear()
lcd.print("     ICU 602         Booting")
time.sleep(0.1)
lcd.clear()
lcd.print("Boot  Successful")
time.sleep(0.1)
lcd.clear()
lcd.print("Dest            Company")

# Initial setup
tempPickedComp = ""
pickedComp = "JWOM"
items = arrays[pickedComp]
current_index = -1
current_index2 = -1
destSelect = False
routeSelect = False
compSelect = False
pickComp = False

while True:
    if is_pressed(button2) and not destSelect and not routeSelect and not pickComp:
        pickComp = True
        current_index2 = (current_index2) % len(Companys)
        tempPickedComp = update_lcd_comp(current_index2)
        time.sleep(1)
    
    if is_pressed(button2) and not destSelect and not routeSelect and pickComp:
        lcd.clear()
        current_index2 = current_index2 % len(Companys)
        lcd.print("Comp Selected")
        time.sleep(2)
        pickedComp = tempPickedComp
        items = arrays[pickedComp]  # Update items with the selected company's routes
        current_index = -1  # Reset current_index for the new list of routes
        destSelect = False
        compSelect = True
        pickComp = False
        main_screen()

    if is_pressed(button1) and not routeSelect and not compSelect and pickComp:
        current_index2 = (current_index2 + 1) % len(Companys)
        tempPickedComp = update_lcd_comp(current_index2)
        time.sleep(0.5)
        
    if is_pressed(button3) and not routeSelect and not compSelect and pickComp:
        current_index2 = (current_index2 - 1) % len(Companys)
        tempPickedComp = update_lcd_comp(current_index2)
        time.sleep(0.5)
    
    if is_pressed(button1) and not routeSelect and not pickComp and compSelect:
        destSelect = True
        current_index = (current_index + 1) % len(items)
        update_lcd(current_index)
        time.sleep(0.2)
        
    if is_pressed(button1) and not routeSelect and not pickComp and not compSelect:
        lcd.clear()
        lcd.print("Pick A Comp")
        time.sleep(0.5)
        main_screen()
        
    if is_pressed(button3) and not routeSelect and not pickComp and not compSelect:
        lcd.clear()
        lcd.print("Pick A Comp")
        time.sleep(0.5)
        main_screen()
        
    if is_pressed(button3) and not routeSelect and compSelect:
        destSelect = True
        current_index = (current_index - 1) % len(items)
        update_lcd(current_index)
        time.sleep(0.2)

    if is_pressed(button2) and destSelect and not routeSelect:
        lcd.clear()
        current_index = current_index % len(items)
        lcd.print("Route Selected")
        time.sleep(2)
        update_lcd(current_index)
        destSelect = False
        routeSelect = True
        current_index = -1
        
    if is_pressed(button2) and not destSelect and routeSelect:
        lcd.clear()
        lcd.print("Route Cleared")
        time.sleep(2)
        main_screen()
        routeSelect = False

