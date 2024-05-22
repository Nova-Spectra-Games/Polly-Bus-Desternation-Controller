# Polly-Bus-Desternation-Controller
This is a recreation of the destination controller in our game Polly bus. It is loaded with routes from Midland Classic and the in-game company JournyWise Of Mainstone.

This project uses a LCD library [^1] from dhalbert to controll the 16x2 1602a LCD we used a [^2]ALAMSCN 2PCS HD44780 1602 16x2 LCD Display

[Amazon Link](https://t.ly/kg7yt)
[^2]: [Amazon Link](https://t.ly/kg7yt)

You will also need

* 3 Buttons
* 10 Male To Male Jumper Cables
* 1 Raspberry Pico/Pico W with Circuit Python [^3]Installed
* 1 Break Board We Used 2
* 1 16x2 1602a LCD
* 1 Mirco USB Cable

[^3]: [Circut Python Install Guide](https://www.youtube.com/watch?v=BRMFH0LI30A)

## Setup the Components
![image](https://github.com/Nova-Spectra-Games/Polly-Bus-Desternation-Controller/assets/170518410/9584b1fd-3079-432c-aad7-1b059351dc3a) 

## Install The Code
* Download the Code From this repo [Link](https://codeload.github.com/Nova-Spectra-Games/Polly-Bus-Desternation-Controller/zip/refs/heads/main)
* More the zip folder to the Raspberry Pi Pico and extract it
* Once the code is extracted make sure you can see code.py in the root of the pico's file structure.
* Now just restart the pico and you can use the button on the small breadboard to control the device.

  
## Add custom routes

* Open routes.py
* Add this template

```python 
CustomRoute = [
  #Route Dest      #Route Num
  "Not In Service  000",
  "Destination     1",
  "Destination     2",
  "Destination     3",
  "Destination     4",
  "Destination     5",
  "Destination     6"
]
```
Make sure to start the route num at the start of the # of the route num comment.
Make sure the last route in the array does NOT have a "," at the end.

Add as many routes as you need.

Now Go to the bottom of routes.py and edit the "arrays" array like this.

```python
arrays = {
    "JWOM": JWOMRoute,
    "MDCL": MDCLRoute,
    "Your Company": CustomRoute,
}
```

And

```python
Companys = ["JWOM", "MDCL", "Your Company"]
```


The LCD library is from [dhalbert](https://github.com/dhalbert/)

[^1]: [LCD Library](https://github.com/dhalbert/CircuitPython_LCD)
