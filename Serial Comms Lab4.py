from machine import UART, Pin
import time

uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1, txbuf=64, rxbuf=64)


while True:
    data2send = input("Enter the message to send: ")
    uart.write(data2send)
    if uart.txdone():
        print("Message not sent successfully")
    else:
        print("Message sent successfully")
    print(uart.read())
    time.sleep(3)
