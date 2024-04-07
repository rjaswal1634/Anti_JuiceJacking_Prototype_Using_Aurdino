import psutil
import serial

# Initialize the serial connection
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to match your Arduino's serial port

def autowrite(driveLetter):
    try:
        # Writing to file removed for sending serial data only
        print("Autowrite executed on:" + driveLetter)
    except:
        print("Write Error on:" + driveLetter)

def check_usb_connected():
    while True:
        partitions = psutil.disk_partitions(all=True)

        for partition in partitions:
            if 'removable' in partition.opts:
                autowrite(partition.mountpoint)
                # Sending serial data to Arduino
                ser.write(b'1\n')  # Sending "1" followed by a newline character
                ser.flush()  # Flush the serial buffer to ensure data is sent immediately

if __name__ == "__main__":
    check_usb_connected()
