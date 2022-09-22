import socket


def connect(addr):
    try:
        HOST = 'localhost'
        BUFFER_SIZE = 1024
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"     
		s.connect(('127.0.0.1',8001))
		s.sendall(payload.encode())
		s.shutdown(socket.SHUT_WR)
		full_data = s.recv(BUFFER_SIZE)
		print(full_data)
	except Exception as e:
		print(e)
	finally:
		s.close()

if __name__ == "__main__":
    main()
