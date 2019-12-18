import easySocket as s
HOST = '127.0.0.1'
PORT = 6666
c, address = s.host_tcp(HOST, PORT)
print("connected to ", address)
data = s.rcv_data(c)
if data:
    if (data.decode() == "hotel1"):
        file = "hotel1.jpg"
    elif (data.decode() == "hotel2"):
        file = "hotel2.jpg"
    print(data)
    s.send_file(file, c)
else:
    s.send_text("error, plz resend",c)