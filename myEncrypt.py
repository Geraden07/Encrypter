#Author: Steven B.
#This work is licensed under the GPL v3
#https://www.gnu.org/licenses/gpl-3.0.html
import os
import getpass
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

#Fill these out:
fileList = [''] #Must be file names (without extension) of the current directory (same as script location)
passwordHash = '' #Must be the value of myHashFunction( loopPass( plainTextPassword ) )

def myHashFunction(password, hashCycles=20):
	"""Function that repeatedly hashes a given password and returns the final hash value.
		Default hash cycles of 20 times.

		Returns string"""
	currentValue = password
	for i in range(hashCycles):
		myHashObject = SHA256.new()
		myHashObject.update(currentValue)
		currentValue = myHashObject.digest()
	return currentValue

def loopPass(password,numOfBytes=32):
	"""Function that loops a password over and over to fill a predetermined number of bytes.
		Default number of bytes is 32.

		Returns string"""
	if len(password)>0:
		while len(password)<numOfBytes:
			password = password + password
		return password[:numOfBytes]

if __name__ == "__main__":
	while 1:
		pwToHash = getpass.getpass('Please enter the password: ')
		if pwToHash != '':
			pwToHash = loopPass(pwToHash)
			hashedPass = myHashFunction(pwToHash)
			if hashedPass==passwordHash:
				encryptionObject = AES.new(pwToHash, AES.MODE_ECB)
				for x in fileList:
					if os.path.isfile(x+'.txt'):
						with open(x+'.txt','rb') as myFile:
							plainText = myFile.read()
						if len(plainText)%16 != 0:
							plainText = plainText + ((16-(len(plainText)%16))*' ')
						cipherText = encryptionObject.encrypt(plainText)
						with open(x+'.txt','wb') as myFile:
							myFile.write(cipherText)
						os.rename(x+'.txt',x+'.AES')
					elif os.path.isfile(x+'.AES'):
						with open(x+'.AES', 'rb') as myFile:
							cipherText = myFile.read()
						plainText = encryptionObject.decrypt(cipherText)
						with open(x+'.AES','wb') as myFile:
							myFile.write(plainText)
						os.rename(x+'.AES',x+'.txt')
				break
			else:
				print 'Error: Wrong password. Try again:'
