import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configure the serial port
SERIAL_PORT = 'COM6'  # Change as needed
BAUD_RATE = 115200      # Adjust based on your device

data_buffer = []
window_size = 5  # Seconds
start_time = time.time()

# Open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Give time to establish the connection


def read_serial():
    """Reads data from the serial port continuously."""
    global data_buffer, start_time
    try:
        if ser.in_waiting > 0:  # Check if data is available
            raw_data = ser.read(ser.in_waiting).decode('utf-8')
            lines = raw_data.strip().split('\n')  # Split multiple lines
            for line in lines:
                try:
                    data_buffer.append(float(line))
                except ValueError:
                    continue

            if time.time() - start_time >= window_size:
                mean_value = np.mean(data_buffer) if data_buffer else 0
                std_dev = np.std(data_buffer) if data_buffer else 0
                count_values = len(data_buffer)
                print(f'Mean of last {window_size} seconds: {mean_value:.2f}')
                print(f'Standard deviation of last {window_size} seconds: {std_dev:.2f}')
                print(f'Number of values captured: {count_values}')
                data_buffer.clear()
                start_time = time.time()
    except ValueError:
        pass

def update(frame):
    """Updates the plot with the captured data."""
    read_serial()
    ax.clear()
    ax.plot(data_buffer, color='blue')
    ax.set_title('Real-Time Data from Serial Port')
    ax.set_ylabel('Value')
    ax.set_xlabel('Samples')

# Set up the figure
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=50)

try:
    plt.show()
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    ser.close()