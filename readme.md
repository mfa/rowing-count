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

### archlinuxarm

pacman:
- i2c-tools
- python-click
- python-scipy
- gcc

pip:
- gpiozero


i2c needs to be enabled!
