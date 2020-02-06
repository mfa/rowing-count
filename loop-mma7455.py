import smbus
import time

bus = smbus.SMBus(1)

# MMA7455L address, 0x1D
bus.write_byte_data(0x1D, 0x16, 0x01)

while True:
    time.sleep(0.01)

    # Read 6 bytes data back from 0x00
    data=bus.read_i2c_block_data(0x1D, 0x00, 6)

    # Convert the data to 10-bits
    xAcc = (data[1] & 0x03) * 256 + data [0]
    if xAcc > 511 :
        xAcc -= 1024
    yAcc = (data[3] & 0x03) * 256 + data [2]
    if yAcc > 511 :
        yAcc -= 1024
    zAcc = (data[5] & 0x03) * 256 + data [4]
    if zAcc > 511 :
        zAcc -= 1024

    # Output data
    print(f"Acceleration {xAcc:5d} {yAcc:5d} {zAcc:5d}")
