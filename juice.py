import serial
import serial.tools.list_ports
import time

print("Juice Jacking is Started")  # Print a message indicating the program has started

# Function to find the port where Arduino is connected
def find_arduino_port():
    # List all available ports and filter out ports with 'Arduino' in description
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description
    ]
    # If Arduino is found, return the port, otherwise return None
    if arduino_ports:
        return arduino_ports[0]
    else:
        return None

# Function to send data to the Arduino
def send_data_to_arduino(arduino_port):
    if arduino_port is not None:  # Check if Arduino port is found
        try:
            # Establish serial connection with Arduino
            ser = serial.Serial(arduino_port, 9600, timeout=1)
            print("Device is found to attack:", arduino_port)  # Print message indicating the device is found
            while True:
                # Sending data to Arduino
                ser.write(b"Your Device is Doomed!\n")  # Send a message to the Arduino
                print("Your Device is Doomed!\n")  # Print a message indicating data sent
                time.sleep(1)  # Wait for 1 second
        except serial.SerialException as e:
            print("Device Ejected after attack")  # Print a message if device is ejected
    else:
        print("Device Not Found or Ejected")  # Print a message if device is not found

# Main program
if __name__ == "__main__":
    while True:
        arduino_port = find_arduino_port()  # Find the port where Arduino is connected
        if arduino_port is not None:  # If Arduino is found
            send_data_to_arduino(arduino_port)  # Send data to Arduino
        else:
            time.sleep(1)  # If Arduino is not found, wait for 1 second and check again
