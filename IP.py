import os

print("COMO SABER MI IP?")
print("-------------------------------------")
ip = input("PARA SABER MI IP PRESIONA (ENTER); ")
print("-------------------------------------")


os.system(' curl -s http://ifconfig.me -w "\n" ')

