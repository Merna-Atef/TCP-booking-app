import easySocket as s
HOST = '127.0.0.1'
PORT = 6666

c = s.connect_tcp(HOST,PORT)
print("client connected on socket ", c)
s.send_text("hotel2", c)
data = s.rcv_data(c)
myfile = open("hotel2r.jpg", 'wb')
myfile.write(data)
