import serial

port = "COM6"  # Change this according to your device
baudrate = 9600

try:
    with serial.Serial(port, baudrate, timeout=1) as ser:
        print(f"Connected to {port} at {baudrate} baud.")

        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                print(line)  # Display real-time data

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")