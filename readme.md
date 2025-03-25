# 🧪 Laboratory Practices - Practice 3 - Redes de sensores electrónicos

This repository contains the third laboratory practice for the **Redes de sensores electrónicos** course. Each section is organized in its own folder and includes the necessary files along with a brief description.
In this practice, we will be using Python as a way to receive data from serial PORT coming from embedded devices.

## 📖 Section Overview

### 📁 Section 1 - 01_pythonProgramToReadSerial
📌 It includes a Python script that uses serial library in order to receive data from listening port.  
📄 Main files:  
- `main.py`: Prints received data through terminal.

### 📁 Section 2 - 02_pythonProgramTxt
📌 Same result as in the previous section, adding functionality to save info on TXT file.
📄 Main files:  
- `main.py`: Writes received data on a TXT file, including a semicolon.

### 📁 Section 3 - 03_interactivePlot
📌 Calculates mean and standard desviation from data recevided and plots it on real time
📄 Main files:  
- `main.py`: plotting on real time the results of received data.
- `Arduino_UART50ms`: generates data to send through UART. 
