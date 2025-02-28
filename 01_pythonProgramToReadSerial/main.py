import serial

port = "COM6"  # Change this according to your device
baudrate = 9600

try:
    with serial.Serial(port, baudrate, timeout=1) as ser, open("serial_output.txt", "w") as file:
        print(f"Connected to {port} at {baudrate} baud.")

        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                formatted_line = line + ";"
                print(formatted_line)  # Display real-time data
                file.write(formatted_line + "\r\n")  # Save data to .txt file with semicolon and carriage return
                file.flush()  # Ensure data is written immediately
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")