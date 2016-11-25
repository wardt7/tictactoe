from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import pickle

client_key = RSA.generate(2048)
encrypt_object = PKCS1_v1_5.new(client_key.publickey())
decrypt_object = PKCS1_v1_5.new(client_key)
message = encrypt_object.encrypt(pickle.dumps({"variable":"hello"}))
print(message)
unencrypted = decrypt_object.decrypt(message,bool)
unencrypted = pickle.loads(unencrypted)
print(unencrypted)
