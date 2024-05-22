# Polly-Bus-Desternation-Controller
This is a recreation of the destination controller in our game Polly bus. It is loaded with routes from Midland Classic and the in-game company JournyWise Of Mainstone

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
