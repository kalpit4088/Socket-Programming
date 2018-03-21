import time
import socket

num = int(raw_input("Enter No. of files"))
files = []

for i in range(num):
	file = raw_input("Enter file to get:")
	files.append(file)

start_t = time.time()

for filename in files:

	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	host = ""
	port = 60001

	try:
		s.connect((host, port))
	except:
		print("error connecting server")
		sys.exit()
	try:
		s.send(filename)
	except:
		print("error sending")
		sys.exit()

	filename = filename.split('/')
	k = len(filename) - 1

	with open(filename[k], 'wb') as f:
	    print 'file opened'
	    while True:
	        print('receiving data...')
	        data = s.recv(1024)
	        # print('data=%s', (data))
	        if not data:
	            break
	        # write data to a file
	        f.write(data)

	f.close()

	print('Successfully got the file')
	s.close()
	print('Connection closed')

print("total time: ",time.time() - start_t)
