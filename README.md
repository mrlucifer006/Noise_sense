
# Noise Monitoring System

## Overview
This Python-based noise monitoring system authenticates users (admins and students) and monitors noise levels using audio input devices. Built with Python 3.10, it uses libraries like `pandas (2.2.3)`, `sounddevice`, `numpy`, and `pywhatkit` to manage CSV-based authentication, process audio and send notifications. The system features a menu-driven interface for selecting user roles and functions. It handles errors for missing CSV files or invalid audio devices. The backend (`datahandle.py`) manages authentication, while the main script (`audio.py`) provides the command-line interface (CLI) and audio processing. This system offers a framework for noise monitoring in settings like schools.

## Features
- **Admins**: Monitor noise on single or multiple devices, receive WhatsApp notifications for high noise and exit the program.
- **Students**: Identify the quietest location based on noise levels.
- **Data Storage**: Uses CSV files (`author.csv`, `student.csv`) for authentication.
- **Audio Processing**: Calculates RMS values to classify noise as "Low" or "High" based on a threshold.
- **Modular Design**: Backend (`datahandle.py`) for authentication, CLI (`audio.py`) for interaction and audio processing.

## Requirements
```
Python 3.10
```
```
pip (latest compatible with Python 3.10)
```
```
pandas 2.2.3
```
```
sounddevice
```
```
numpy
```
```
pywhatkit
```
## Installation
1. Clone the repository (if hosted):
   ```
   https://github.com/mrlucifer006/Noise_sense
   ```
2. Install Python 3.10 and ensure the latest `pip` version:
   ```
   python3.10 -m ensurepip --upgrade
   python3.10 -m pip install --upgrade pip
   ```
3. Install dependencies:
   ```
   pip install pandas==2.2.3 sounddevice numpy pywhatkit
   ```
4. Place `author.csv` and `student.csv` in the script directory.
5. Ensure audio input devices are connected.

## Usage
1. Run the main script:
   ```
   python audio.py
   ```
2. Select a user type (Admin/Student/Exit) and follow prompts:
   - **Admin**: Log in to check noise levels, monitor continuously, or exit.
   - **Student**: Log in to find the quietest location.
   - **Exit**: Terminate the program.

## Contributing
- Fork the repository and submit a pull request with changes.
- Report issues or suggest features via the Issues tab (if hosted).
- Follow Python best practices and include clear comments.

## License
GPL-3.0 License - free to use, modify, and distribute this project. Copyright (c) 2025 [Project Contributors]. See <https://www.gnu.org/licenses/> for details.
