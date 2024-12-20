from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64encode
from base64 import b64decode
import socket


#generates cipher and decrypts message using given public key
def verify(plaintext, key, signature):
	#Set key for cipher generation
	Key = RSA.import_key(key)
	#Generate the RSA cipher for encryption
	mHash = SHA256.new(plaintext)
	#encrypt plaintext
	try:
		pkcs1_15.new(Key).verify(mHash, signature)
		print(plaintext.decode('utf-8'))
		print('message verified')
	except(ValueError,TypeError):
		print('compromised connection')	
		


if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 30377
	#connect the socket to the local machine on the designated port
	s.connect(('127.0.0.1', port))
	
	#parse the received data
	publicKey = s.recv(2048)
	signature = s.recv(256)
	mData = s.recv(1024).decode()
	#encode message since it was encoded and decoded we utf-8 encode it to sign it
	plaintext = mData.encode('utf-8')
	
	o = input('Would you like to modify the message?(y/n):')
	if o == 'y':
		byte_array = bytearray(signature)
		byte_array[0] = ord('A')
		sig1 = byte_array
		verify(plaintext, publicKey, sig1)
	else:
		#verify
		verify(plaintext, publicKey, signature)
	
	
	

	
	
