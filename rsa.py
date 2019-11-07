import M2Crypto
import base64
​
# pubkey from client
pubkey_fromdb = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp3AkkjJl7RLYfaFZr5rgiuOo9fHp3PEJ\nLXBzN5azKC7oMrxE6PkOXJxe8zbsjlngM+v/reqNpRnJehzeGZ7ZiaWgfiNU6qaM9AMT1CMIdC2x\nlexod0HSz/XsyBcC8Pcoj6Oay9r+iJljRoiv2X1ErkbtIVqurDta8osADLAxoiBcEugr05o819by\nWpKwOaVW4HrqKfmQcyKcL3H4ZSIT1UXJtt8LMi1dxwB3QwjFLBli4r/TpVV0G0hRPBMvG4merFiH\nyLGikBoiKZgY7IoXkoATdLZDWKGCqukMZ8KlrJf2MjQA73rziPKL753bzTCW0JzMaDVdJx9yYLKU\ntA9o4QIDAQAB'
​
# save to .pem
pubkey_pem = '-----BEGIN PUBLIC KEY-----\n' + pubkey_fromdb + '\n-----END PUBLIC KEY-----'
print(pubkey_pem)
f = open("pub_key.pem", 'w')
f.write(pubkey_pem)
f.close()
​
public_key = M2Crypto.RSA.load_pub_key('pub_key.pem')
​
​# plain text
data = "여기에 암호화할 문장"
data_input = base64.b64encode(data.encode('utf-8'))
ciphertext = public_key.public_encrypt(data.encode('utf-8'), M2Crypto.RSA.pkcs1_padding)
encrypted_message = str(base64.b64encode(ciphertext), 'utf8')

# send to client encrypted_message
print("클라이언트로 보내줄 문장  = " + encrypted_message)