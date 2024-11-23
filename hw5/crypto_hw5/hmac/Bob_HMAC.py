from base64 import b64encode
from base64 import b64decode
import hashlib
import socket
import hmac

	
def verify(plaintext, key, sig1):
	#verify the message by checking the original signature against a newly generated one
	sig2 = hmac.new(key, plaintext, hashlib.sha256).digest()

	if(sig1 == sig2):
		print('message verified')
	else:
		print('compromised connection')	

if __name__ == '__main__':
	#socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 30370
	#estabolish connection
	s.connect((host, port))
	#receive data
	sig = s.recv(1024)
	m = s.recv(1024).decode()
	k = s.recv(1024)
	
	o = input("Would you like to change the value?(y/n): ")
	
	if o == 'y':
		byte_array = bytearray(sig)
		byte_array[0] = ord('A')
		sig1 = byte_array
		verify(m.encode(), k, sig1)
	else:
		verify(m.encode(), k, sig)
	
	

		
			
