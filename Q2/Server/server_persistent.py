import socket

port = 9998
s = socket.socket()
host = ""

try:
    s.bind((host, port))
except:
    print('Binding error')

s.listen(5)
print 'Server listening....'

conn, addr = s.accept()
while True:
    print 'Connection Established with Client'
    filename = conn.recv(1024)
    print filename

    try:
        f = open(filename,'rb')
    except:
        print('error opening file or file does not exist')

    l = f.read(1024)
    while (l):
       conn.send(l)
       # print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    print('Done sending')
conn.close()
