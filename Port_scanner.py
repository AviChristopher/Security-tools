import socket    # networking tool

t = "Add target or Ip Address" # Add target/ IP Address

print(f"Scanning {t}....\n")

for port in range (1, 65535):   #Testing ports one by one
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a connection tool in the module socket
    socket.setdefaulttimeout(1)

    result= s.connect_ex((t, port )) # method tries to connect to the IP and ports

    if result == 0:    #Then prints the port thats open
        print(f"Port {port} is open")

    s.close()




