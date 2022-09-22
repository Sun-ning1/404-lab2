import socket,time
from multiprocessing import Process

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

def main():
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST,PORT))
		s.listen(2)
		while True:
			conn,addr = s.accept()
			p = Process(target = multi_echo,args=(addr,conn))
			p.daemon = True
			p.start()
			print("Started process ",p)

def multi_echo(addr,conn):
	full_data = conn.recv(BUFFER_SIZE)
	conn.sendall(full_data)
	conn.shutdown(socket.SHUT_WR)
	conn.close()

if __name__ == '__main__':
	main()