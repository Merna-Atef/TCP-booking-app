import easySocket as s
import numpy
array = []
while 1:
    HOST = '192.168.43.218'
    PORT = 6666
    print('hey there')
    c, address = s.host_tcp(HOST, PORT)
    print("connected to ", address)
    data = s.rcv_data(c)
    if data:
        if (data.decode() == "hotel1"):
            file1 = "hotel1.jpg"
            s.send_file(file1, c)
        elif (data.decode() == "hotel2"):
            file1 = "hotel2.jpg"
            s.send_file(file1, c)
        elif (data.decode() == "hotel1video"):
            file1 = "leysbeu.mp4"
            s.send_file(file1, c)
        elif (data.decode() == "hotel2video"):
            file1 = "dalen.mp4"
            s.send_file(file1, c)
        elif (data.decode() == "save"):
            array.append("Other Client")
            with open('UserData.txt', 'w') as filehandle:
                for listitem in array:
                    filehandle.write('%s\n' % listitem)
        else:
            array.append(data.decode())
            print(data)
    else:
        s.send_text("error, plz resend",address)