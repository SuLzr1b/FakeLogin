# FakeLoginEducacional

A Python tool with a graphical interface (Tkinter) for simulating fake login screens to study phishing techniques, built for educational purposes.

**WARNING**: This project is for educational purposes only. Do not use to collect real credentials or deceive users. Unauthorized use may violate laws, such as Brazil's General Data Protection Law (LGPD).

## Purpose
This project is designed to help cybersecurity students understand how phishing attacks collect credentials through fake login interfaces. It provides a graphical login screen, logs user inputs, and demonstrates social engineering techniques in a controlled, ethical environment.

## Features
- Simulates a login interface with a Tkinter GUI, including username and password fields.
- Logs all login attempts with timestamps to `login_settings.txt`.
- Displays "invalid credentials" to mimic a phishing attempt.
- Includes ethical warnings in the code and interface to ensure responsible use.
- Allows multiple login attempts with clear feedback via popups.

## Requirements
- Python 3.x (with Tkinter included; typically pre-installed on Windows)
- No external libraries required

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FakeLogin.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FakeLogin
   ```

## Usage
1. Run the tool:
   ```bash
   python gui.py
   ```
2. A graphical window will appear:
   - Enter a username and password.
   - Click "Login" to log the attempt and see "invalid credentials" popup.
   - Click "Sair" to close the application.
3. Check `login_settings.txt` for the recorded attempts.

**Note**: Always test in a controlled environment with explicit permission. Do not use to collect real credentials.

## Example Log (`login_settings.txt`)
```
2025-04-28 21:30:15.123456: User: John, Password: 123
2025-04-28 21:30:16.234567: User: Brow, Password: 321
```

## Ethical Considerations
This tool is strictly for educational purposes, such as learning about phishing and social engineering in cybersecurity. Do not use it to collect credentials or deceive users, as this may violate privacy laws, including Brazil’s LGPD. Always obtain permission and test in a controlled environment.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
