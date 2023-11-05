# count rowing of my rowing machine

## about

Use raspberry pi zero W applied to a Hanseatic Rowing Machine using cable ties.

Blogpost: https://madflex.de/posts/count-rows-on-an-old-rowing-machine/

## sensor

- currently supported: MMA7455
- https://www.nxp.com/docs/en/data-sheet/MMA7455L.pdf

## requirements

### python packages

- smbus
- click
- scipy / numpy
- gpiozero

### raspios (bookworm)

activate i2c in raspi-config

```
sudo apt install i2c-tools virtualenv
virtualenv venv
. venv/bin/activate
pip install click scipy gpiozero smbus
```
