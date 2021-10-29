This Library is developed for data Encryption and Decryption.

you can encrypt or decrypt just a character or a set of data at once of any format.

like:

	Strings
	Integers
	Float
	Lists
	Tuples
	Sets
	Dictionaries
Or you can also Encrypt or Decrypt a Nested Data types
like:
	
    [1,2,"abc","A"(4.5,{6,7,"a",{"name":"Gajendra","studying":12},"hi"},['this is an Example'])]
    
Syntax :

import EnDecoder as endc


Data = [1,2,"abc","A"(4.5,{6,7,"a",{"name":"Gajendra","studying":12},"hi"},['this is an Example'])]

Encrypted_Data = endc.encrypt(Data)


# To Decrypt Encrypted Data
Decrypted_Data = endc.decrypt(Encrypted_Data)

