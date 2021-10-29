"""
Name : 'EnDecoder'
Version : '2.0.1'
Owner : 'GS Tech'
Date of Creation : '27/10/2021'
last Updated : '28/10/2021'
Programmer : 'Gajender'

"""
" Encryptor Starts From Here"

def encrypt(key):
    if key == "" or key == None:
        return 0

    # Float Encryption
    elif type(key) == float:
        _key = str(key)
        n = 0
        _encrypted = ""
        while n <= len(_key)-1:
            _unicode = ord(_key[n])
            _encrypt_key = int(_unicode*256-36/2)
            _encrypted = _encrypted + chr(_encrypt_key)
            n = n+1
        _encrypted = _encrypted + "旮毮滮惮珮"
        return _encrypted

    # Integer Encryption
    elif type(key) == int:
        _key = str(key)
        n = 0
        _encrypted = ""
        while n <= len(_key)-1:
            _unicode = ord(_key[n])
            _encrypt_key = int(_unicode*256-36/2)
            _encrypted = _encrypted + chr(_encrypt_key)
            n = n+1
        _encrypted = _encrypted + "森淮珮"
        return _encrypted

    # List Encryption
    elif type(key) == list:
        _encrypted = []
        for _key in key:
            _encrypted.append(encrypt(_key))
        return _encrypted

    # Tuple Encryption
    elif type(key) == tuple:
        _encrypted = []
        for _key in key:
            _encrypted.append(encrypt(_key))
        return tuple(_encrypted)

    # Set Encryption
    elif type(key) == set:
        _encrypted = []
        for _key in key:
            _encrypted.append(encrypt(_key))
        return set(_encrypted)

    # Dictionary Encryption
    elif type(key) == dict:
        _encrypted = {}
        _keys = []
        _values = []
        _key = list(key.keys())
        _value = list(key.values())
        for _nkey in _key:
            _keys.append(encrypt(_nkey))
        for _nkey in _value:
            _values.append(encrypt(_nkey))
        for _data in range(len(_keys)):
            _encrypted[_keys[_data]] = _values[_data]
        return _encrypted

    # String or Others Encryption
    else:
        _key = str(key)
        n = 0
        _encrypted = ""
        while n <= len(_key)-1:
            _unicode = ord(_key[n])
            _encrypt_key = int(_unicode*256-36/2)
            _encrypted = _encrypted + chr(_encrypt_key)
            n = n+1
        return _encrypted


"""

                                    Decryptor Starts From Here



"""



def decrypt(key):
    if key == "" or key == None:
        return 0

    # List Decryption
    elif type(key) == list:
        _decrypted = []
        for _key in key:
            _decrypted.append(decrypt(_key))
        return _decrypted
    # Tuple Decryption
    elif type(key) == tuple:
        _decrypted = []
        for _key in key:
            _decrypted.append(decrypt(_key))
        return tuple(_decrypted)

    # Set Decryption
    elif type(key) == set:
        _decrypted = []
        for _key in key:
            _decrypted.append(decrypt(_key))
        return set(_decrypted)

    # Dictionary Decryption
    elif type(key) == dict:
        _decrypted = {}
        _keys = []
        _values = []
        _key = list(key.keys())
        _value = list(key.values())
        for _nkey in _key:
            _keys.append(decrypt(_nkey))
        for _nkey in _value:
            _values.append(decrypt(_nkey))
        for _data in range(len(_keys)):
            _decrypted[_keys[_data]] = _values[_data]
        return _decrypted

    # String, Integer, Float or Others Decryption
    else:
        _key = str(key)
        _decrypted = ""
        for _nkey in _key:
            _unicode = ord(_nkey)
            _decrypt_key = int((_unicode+36/2)/256)
            _decrypted = _decrypted + chr(_decrypt_key)
        try:
            if "int" in _decrypted:
                _convert = int(_decrypted[:len(_decrypted)-3])
                return _convert
            elif "float" in _decrypted:
                _convert = float(_decrypted[:len(_decrypted)-5])
                return _convert
            else:
                return _decrypted
        except:
            return _decrypted
