import serial
import sys
import threading

COM_PORT = 'COM5'
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

def read_from_port(ser):
    while True:
        if ser.in_waiting:
            mcu_feedback = ser.readline().decode().strip()

            if mcu_feedback.startswith("Distance in CM: "):
                try:
                    distance = int(mcu_feedback[16:])
                    if distance > 15:
                        print('No yusha detect...')
                    else:
                        print('Too close, Servo speedup, it is time to go to isekai!!!')
                except ValueError:
                    print('Invalid distance value received:', mcu_feedback)
    
            print('Arduino reaction:', mcu_feedback)
            if mcu_feedback.lower() == 'e':
                ser.close()
                print('bye!')
                sys.exit()

def listen_for_exit():
    while True:
        end = input('press e to exit').lower()
        if end == 'e':
            ser.close()
            print('bye!')
            sys.exit()

try:
    thread = threading.Thread(target=read_from_port, args=(ser,))
    thread.daemon = True
    thread.start()
    listen_for_exit()
except KeyboardInterrupt:
    ser.close()
    print('bye!')
