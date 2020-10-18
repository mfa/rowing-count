import csv
import smbus
import time
import datetime
import signal

import warnings
warnings.simplefilter('ignore')
import gpiozero


led = gpiozero.LED(19)  # pin 35
bus = smbus.SMBus(1)
# MMA7455L address, 0x1D
bus.write_byte_data(0x1D, 0x16, 0x01)


global quit


def handle_interrupt(*args):
    quit = True


if __name__ == "__main__":
    led.on()
    signal.signal(signal.SIGINT, handle_interrupt)
    quit = False

    fieldnames = ["dt", "xAcc_mma7455", "yAcc_mma7455", "zAcc_mma7455"]
    logpath = f"/home/alarm/logs/{datetime.datetime.now().isoformat()}.csv"
    with open(logpath, "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        while not quit:
            time.sleep(0.01)

            # Read 6 bytes data back from 0x00
            data = bus.read_i2c_block_data(0x1D, 0x00, 6)

            # Convert the data to 10-bits
            xAcc = (data[1] & 0x03) * 256 + data[0]
            if xAcc > 511:
                xAcc -= 1024
            yAcc = (data[3] & 0x03) * 256 + data[2]
            if yAcc > 511:
                yAcc -= 1024
            zAcc = (data[5] & 0x03) * 256 + data[4]
            if zAcc > 511:
                zAcc -= 1024

            data = {
                "dt": datetime.datetime.now().isoformat(),
                "xAcc_mma7455": xAcc,
                "yAcc_mma7455": yAcc,
                "zAcc_mma7455": zAcc,
            }
            writer.writerow(data)
    led.off()
