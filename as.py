>>> from Crypto.Cipher import AES
>>> obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')              
>>> obj
>>> message = "Hello IOT"
>>> ciphertext = obj.encrypt(message)
>>> ciphertext
>>> obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')			
>>> message= obj2.decrypt(ciphertext)
>>> print message
>>> obj2 = AES.new('This is a key951', AES.MODE_CFB, 'This is an IV456')            
>>> message= obj2.decrypt(ciphertext)
>>> print message

