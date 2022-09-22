import socket,time,sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024
def get_remote_ip(host):
	print('Getting IP for {}'.format(host))
	try:
		remote_ip = socket.gethostbyname(host)
	except socket.gaierror:
		print('Hostname could not be resolved. Exiting')
		sys.exit()

	print('Ip address of {} is {}'.format(host,remote_ip))
	return remote_ip

def main():
	host = 'www.google.com'
	port = 80
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as pstart:
		print('Starting proxy server')
		pstart.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		pstart.bind((HOST,PORT))
		pstart.listen(1)
		while True:
			conn,addr = s.accept()
			print('Connected by',addr)
			with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as pend:

				send_full_data = conn.recv(BUFFER_SIZE)
				data_string = send_full_data.decode()
                print("Connecting to {}".format(host))
				remote_ip = get_remote_ip(host)
				pend.connect((remote_ip,port))


			conn.close()

if __name__ == "__main__":
	main()