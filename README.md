# Keylogger
 Trojan keylogger application developed in Python for Windows systems

It consists of two main components:

- **`keylogger.py`**: Captures keystrokes from the target machine and sends the data to a remote server via a TCP connection. It is built into a standalone `.exe` file for ease of deployment.

- **`listener.py`**: Runs on the server machine, listens for incoming connections from the keylogger, and logs the received keystrokes into a file named `log.txt`.

**Key Features**:
- **Standalone Executable**: Convert `keylogger.py` into a `.exe` file for deployment on Windows systems.
- **Stealth Operation**: Runs without showing a console window on the target machine.
- **Remote Logging**: Captured keystrokes are sent to a remote server and saved in `log.txt` for monitoring.

**Usage**:
1. Compile `keylogger.py` into an executable using `build.py`.
2. Run `listener.py` on the server to start receiving and logging keystrokes.
3. Deploy the compiled `keylogger.exe` on the target machine.

**Important Note**:
This software is intended for educational and research purposes only. Unauthorized use on systems without explicit consent is illegal and unethical.
