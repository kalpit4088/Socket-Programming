import socket
import time

s = socket.socket()
host = ""
port = 9998

try:
	s.connect((host, port))
except:
	print('error connecting server')
	sys.exit()

num = int(raw_input("Enter No. of files"))
files = []

for i in range(num):
	file = raw_input("Enter file to get:")
	files.append(file)

start_t = time.time()
for filename in files:
	try:
		s.send(filename)
	except:
		print('error sending file')


	filename = filename.split('/')
	k = len(filename) - 1
	with open(filename[k], 'wb') as f:
	    print 'file opened'
	    while True:
	        print('receiving data...')
	        data = s.recv(1024)
	        # print('data=%s', (data))
	        f.write(data)
	        if len(data) < 1024:
	            break
	        # write data to a file

	f.close()
	print('Successfully get the file')
print (time.time() - start_t)

s.close()
print('connection closed')
